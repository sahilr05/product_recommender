import random
from typing import Dict
from typing import List
from typing import Union

from django.db import transaction

from .models import Order
from .models import OrderProduct
from .models import Product


def recommend_products(product_id: str) -> Dict[str, List[Union[str, int]]]:
    """Return recommended products for a product with the given ID."""
    try:
        recommendations = {}

        # Retrieve pre-calculated similar products
        similar_products = get_precomputed_similar_products(product_id)
        recommendations["similar_products"] = similar_products.values()

        # Retrieve pre-calculated frequently bought together products
        frequently_bought_together = get_precomputed_frequently_bought_together(
            product_id
        )
        recommendations[
            "frequently_bought_together"
        ] = frequently_bought_together.values()

        return recommendations
    except Product.DoesNotExist:
        return {}


def get_precomputed_similar_products(product_id: str) -> List[Product]:
    """Return similar products for a product with the given ID."""
    product = Product.objects.get(product_id=product_id)
    similar_products = product.similar_products.all()

    return similar_products


def get_precomputed_frequently_bought_together(product_id: str) -> List[Product]:
    """Return frequently bought together products for a product with the given ID."""

    product = Product.objects.get(product_id=product_id)
    frequently_bought_together = product.frequently_bought_together.all()

    return frequently_bought_together

@transaction.atomic
def create_order(
    *,
    product_id: str,
    price: float,
    currency_code: str,
    quantity: int,
    address: str,
    payment_mode: str
) -> OrderProduct:
    """Create an order with the given data."""
    product = Product.objects.get(product_id=product_id)
    order = Order.objects.create(
        code=random.randint(100000, 999999),
        address=address,
        payment_mode=payment_mode,
    )
    OrderProduct.objects.create(
        product=product,
        order=order,
        price=price,
        currency_code=currency_code,
        quantity=quantity,
    )
    return order


@transaction.atomic
def remove_product_from_order(*, product_id: str, order_id: str) -> None:
    """Remove a product with the given ID from an order with the given ID."""
    OrderProduct.objects.filter(product_id=product_id, order_id=order_id).delete()


@transaction.atomic
def add_product_to_order(
    *, product_id: str, order_id: str, price: float, currency_code: str, quantity: int
) -> None:
    """Add a product to an order with the given ID."""
    OrderProduct.objects.create(
        product_id=product_id,
        order_id=order_id,
        price=price,
        currency_code=currency_code,
        quantity=quantity,
    )
    return Order.objects.get(order_id=order_id)

def get_order_details(order_id: str) -> Order:
    return Order.objects.get(order_id=order_id)