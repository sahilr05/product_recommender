import uuid

from .types import ProductCategory, states_as_list
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
    pass

class OrderProduct(BaseModel):
    pass