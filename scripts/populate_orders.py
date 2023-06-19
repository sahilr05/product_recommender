import uuid
from decimal import Decimal
from api.types import states_as_values, ProductCategory, PaymentMode, CurrencyCode
from api.models import Order, OrderProduct, Product
from faker import Faker
from django.db import transaction

fake = Faker()

def create_order():
    address = fake.address()
    payment_mode = get_random_payment_mode()
    code = fake.random_number(digits=6)

    order = Order.objects.create(
        order_id=uuid.uuid4(),
        address=address,
        payment_mode=payment_mode,
        code=code
    )

    return order

def get_random_product():
    products = Product.objects.all()
    return fake.random_element(products)

def get_random_payment_mode():
    payment_modes = states_as_values(PaymentMode)
    return fake.random_element(payment_modes)

def create_order_product(order, product, quantity, price, currency_code):
    order_product = OrderProduct.objects.create(
        entry_id=uuid.uuid4(),
        product=product,
        order=order,
        quantity=quantity,
        price=price,
        currency_code=currency_code
    )

    return order_product

@transaction.atomic
def run():
    # Create sample orders
    for _ in range(10):
        order = create_order()

        # Add random products to the order
        for _ in range(3):
            product = get_random_product()
            quantity = fake.random_int(min=1, max=5)
            price = Decimal(fake.random_int(min=100, max=1000))
            currency_code = CurrencyCode.USD

            create_order_product(order, product, quantity, price, currency_code)

    print('Order and OrderProduct data has been populated successfully.')
