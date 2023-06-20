from collections import Counter
from django.db.models import Count
from celery import shared_task
from celery.schedules import crontab
from .models import Product, OrderProduct, Order
from django.db import transaction
from product_recommendation_system.celery import app
    
@shared_task
def update_product_recommendations():
    products = Product.objects.all()

    for product in products:
        # Find similar orders
        similar_products = find_similar_products(product)
        product.similar_products.set(similar_products)

        # Find frequently bought together orders
        frequently_bought_together = find_frequently_bought_together(product)
        product.frequently_bought_together.set(frequently_bought_together)

    return "Product recommendations updated successfully"


def find_similar_products(product):
    # Find products in the same category excluding the current product
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return similar_products


def find_frequently_bought_together(product):
    # Find products that are frequently bought together with the given product
    order_product_entries = OrderProduct.objects.filter(product__product_id=product.product_id)

    # Find all orders that contain the target product
    target_order_ids = set(order_product_entries.values_list('order_id', flat=True))

    frequently_bought_together = []

    # Iterate over the orders and find frequently bought together products
    for order_id in target_order_ids:
        other_products = OrderProduct.objects.filter(order_id=order_id).exclude(product__product_id=product.product_id)

        frequently_bought_together.extend(other_products.values_list("product_id", flat=True))


    # Count the frequency of each product and sort by frequency
    frequently_bought_together = Counter(frequently_bought_together)
    frequently_bought_together = dict(frequently_bought_together.most_common(5))

    return Product.objects.filter(product_id__in=frequently_bought_together.keys())

app.conf.beat_schedule = {
    "ping-task": {
        "task": "api.recommender.update_product_recommendations",
        "schedule": crontab(minute="*", hour="*"),
    }
}
