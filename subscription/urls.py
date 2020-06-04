from django.urls import path
from .views import (
    user_subscriptions,
    subscrition_detail

)

app_name = 'subscription'
urlpatterns = [
    path('subscriptions', user_subscriptions, name='subscription'),
    path('subscriptions/<id>', subscrition_detail, name='unsubscribe')
]
