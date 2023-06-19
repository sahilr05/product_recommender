import uuid

from .types import ProductCategory, states_as_list, CurrencyCode, PaymentMode
from django.db import models


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=states_as_list(ProductCategory),max_length=100)

    def __str__(self):
        return self.title


class Specification(BaseModel):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)


class Order(BaseModel):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.TextField()
    payment_mode = models.CharField(choices=states_as_list(PaymentMode), max_length=100)


class OrderProduct(BaseModel):
    entry_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency_code = models.CharField(choices=states_as_list(CurrencyCode), max_length=100)