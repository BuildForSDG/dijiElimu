import stripe
from dijielimu import settings


def get_or_create_stripe_subscriber(email, token):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    connected_customers = stripe.Customer.list()
    for customer in connected_customers:
        if customer.email == email:
            print(f'{email} found')
            stripe.Account.modify_capability(
                settings.STRIPE_ACC,
                "card_payments",
                requested=True,
            )
            return customer
    print(f'{email} created')
    return stripe.Customer.create(
        email=email,
        source='tok_br',
    )
