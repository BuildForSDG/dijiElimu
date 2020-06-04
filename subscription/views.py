import stripe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes
    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication
    )
from .models import Subscription
from .serializers import SubscriptionSerializer
from dijielimu import settings
from .stripe import get_or_create_stripe_subscriber
from course.models import Course
from users.serializers import TokenSerializer


@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated, ])
def subscrition_detail(request, id):
    user = TokenSerializer(request.auth).data.get('auth_user')
    try:
        subscrition = Subscription.objects.get(
            id=id, user__id=user['id'], is_active=True)
    except Subscription.DoesNotExist as e:
        return Response({'error': e.args[0]}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SubscriptionSerializer(
            subscrition, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            course = serializer.data['subscribed_course']
            course_obj = Course.objects.get(id=course['id'])
            course_obj.unsubscribe(user, course_obj)
            return Response(
                {'message': f'You Unsubscribed to {course["name"]}'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = SubscriptionSerializer(subscrition)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        subscrition.delete()
        return Response(
            {'message': 'subcription deleted'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['POST', 'GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated, ])
def user_subscriptions(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    user = TokenSerializer(request.auth).data.get('auth_user')
    if request.method == 'POST':
        subscriber = {'user': user.id}
        query = {**data, **subscriber}
        serializer = SubscriptionSerializer(data=query)
        if serializer.is_valid():
            course = Course.objects.get(id=query.get('course')).course_name
            try:
                subscriber = get_or_create_stripe_subscriber(
                    request.user.email,
                    data.get('stripe_token'),
                )
                charge = stripe.Charge.create(
                    amount=query['amount'],
                    currency='usd',
                    customer=subscriber,
                    description=query['description'],
                )
                if charge:
                    serializer.save()
                    return Response(
                        {
                            'message': f'subscribed to {course} successfully'
                        },
                        status=status.HTTP_201_CREATED
                    )
            except stripe.error.StripeError as e:
                if e.error is None:
                    return Response(
                        {'error': 'Connection to stripe server failed'},
                        status=e.http_status)
                return Response(
                    {'error': e.error.message},
                    status=e.http_status)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            serializer = SubscriptionSerializer()
            queryset = Subscription.objects.filter(
                user__id=user['id'], is_active=True)
            serializer = SubscriptionSerializer(
                queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
