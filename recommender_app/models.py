import uuid
from datetime import datetime
from typing import Optional

from django.db import models

from .types import CurrencyCode
from .types import PaymentMode
from .types import ProductCategory
from .types import states_as_list


class BaseModel(models.Model):
    """
    Base model for all models in the application.

    Attributes:
        created_at (datetime): The datetime when the object was created.
        modified_at (datetime): The datetime when the object was last modified.
        deleted_at (Optional[datetime]): The datetime when the object was deleted (if applicable).
    """

    created_at: datetime = models.DateTimeField(auto_now_add=True)
    modified_at: datetime = models.DateTimeField(auto_now=True)
    deleted_at: Optional[datetime] = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    product_id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # UUID of the product
    code: str = models.CharField(max_length=200)  # Code of the product
    name: str = models.CharField(max_length=100)  # Name of the product
    description: Optional[str] = models.TextField(
        null=True, blank=True
    )  # Description of the product, optional
    category: str = models.CharField(
        choices=states_as_list(ProductCategory), max_length=100
    )  # Category of the product
    similar_products: models.ManyToManyField = models.ManyToManyField(
        "self"
    )  # Many-to-many relationship with similar products
    frequently_bought_together: models.ManyToManyField = models.ManyToManyField(
        "self"
    )  # Many-to-many relationship with frequently bought together products

    def __str__(self) -> str:
        """Return the name of the product as a string."""
        return self.name


class Specification(BaseModel):
    name: str = models.CharField(max_length=100)  # Name of the specification
    value: str = models.CharField(max_length=100)  # Value of the specification
    product: Product = models.ForeignKey(
        Product, related_name="specifications", on_delete=models.CASCADE
    )  # Foreign key to the product, with related name 'specifications'. Many-to-one relationship


class Order(BaseModel):
    order_id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # UUID of the order
    code: str = models.CharField(max_length=100)  # Code of the order
    address: str = models.TextField()  # Address for the order
    payment_mode: str = models.CharField(
        choices=states_as_list(PaymentMode), max_length=100
    )  # Payment mode for the order

    def __str__(self) -> str:
        """Return the code of the order as a string."""
        return self.code

    @property
    def order_products(self):
        return OrderProduct.objects.filter(order_id=self.order_id)


class OrderProduct(BaseModel):
    entry_id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # UUID of the order product entry
    product: Product = models.ForeignKey(
        Product, related_name="order_products", on_delete=models.CASCADE
    )  # Foreign key to the product, with related name 'order_products'. Many-to-one relationship
    order: Order = models.ForeignKey(
        Order, related_name="order_products", on_delete=models.CASCADE
    )  # Foreign key to the order, with related name 'order_products'. Many-to-one relationship
    quantity: int = models.PositiveIntegerField()  # Quantity of the product ordered
    price: float = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Price of the product
    currency_code: str = models.CharField(
        choices=states_as_list(CurrencyCode), max_length=100
    )  # Currency code for the price of the product

    def __str__(self) -> str:
        """Return the code and name of the product for the order product entry as a string."""
        return f"{self.order.code} {self.product.name}"
