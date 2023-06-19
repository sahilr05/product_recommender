from .models import Product, OrderProduct, Order
from django.db import transaction
import random

def recommend_products(product_id):
    try:
        recommendations = {}

        # Retrieve pre-calculated similar products
        similar_products = get_precomputed_similar_products(product_id)
        recommendations['similar_products'] = similar_products.values()

        # Retrieve pre-calculated frequently bought together products
        frequently_bought_together = get_precomputed_frequently_bought_together(product_id)
        recommendations['frequently_bought_together'] = frequently_bought_together.values()

        return recommendations
    except Product.DoesNotExist:
        return {}

def get_precomputed_similar_products(product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        similar_products = product.similar_products.all()

        return similar_products
    except Product.DoesNotExist:
        return []

def get_precomputed_frequently_bought_together(product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        frequently_bought_together = product.frequently_bought_together.all()

        return frequently_bought_together
    except Product.DoesNotExist:
        return []

@transaction.atomic
def create_order(*, product_id, price, currency_code, quantity, address, payment_mode):
    product = Product.objects.get(product_id=product_id)
    order = Order.objects.create(
        code = random.randit(100000, 999999),
        address = address,
        payment_mode = payment_mode,
    )
    return OrderProduct.objects.create(
        product = product,
        order = order,
        price = price,
        currency_code = currency_code,
        quantity = quantity,
    )

@transaction.atomic
def remove_product_from_order(*, product_id, order_id):
    OrderProduct.objects.filter(product_id=product_id, order_id=order_id).delete()

@transaction.atomic
def add_product_to_order(*, product_id, order_id, price, currency_code, quantity):
    OrderProduct.objects.create(
        product_id=product_id,
        order_id=order_id,
        price=price,
        currency_code=currency_code,
        quantity=quantity,
    )