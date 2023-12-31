import uuid
from django.core.management.base import BaseCommand
from recommender_app.models import Product, Specification, ProductCategory
from faker import Faker
from django.db import transaction

fake = Faker()


def create_product(
    code: str, name: str, description: str, category: str
) -> Product:
    """Create a Product instance with the given data and specifications."""
    product = Product.objects.create(
        product_id=uuid.uuid4(),
        code=code,
        name=name,
        description=description,
        category=category,
    )

    # Create specifications for the product
    create_specification(product, "Color", fake.color_name())
    create_specification(product, "Brand", fake.company())
    create_specification(product, "Price", fake.random_int(min=100, max=1000))
    # Add more specifications as needed

    return product


def create_specification(product: Product, name: str, value: str) -> Specification:
    """Create a Specification instance with the given data and associate it with a product."""
    specification = Specification.objects.create(name=name, value=value, product=product)
    return specification


@transaction.atomic
def run():
    """Populate the Product and Specification models with sample data."""
    # Create product categories
    electronics_category = ProductCategory.ELECTRONICS
    cases_covers_category = ProductCategory.CASES_AND_COVERS
    accessories_category = ProductCategory.HOME_UTILITIES

    # Create mobile phones
    iphone = create_product(
        code="IPH001",
        name="iPhone",
        description="Smartphone by Apple",
        category=electronics_category,
    )
    samsung_galaxy = create_product(
        code="SAM001",
        name="Samsung Galaxy",
        description="Smartphone by Samsung",
        category=electronics_category,
    )

    # Create covers for mobile phones
    create_product(
        code="IPH_COVER001",
        name=fake.word().capitalize() + " Cover for iPhone",
        description=fake.sentence(),
        category=cases_covers_category,
    )
    create_product(
        code="SAM_COVER001",
        name=fake.word().capitalize() + " Cover for Samsung Galaxy",
        description=fake.sentence(),
        category=cases_covers_category,
    )

    # Create charges for mobile phones
    create_product(
        code="IPH_CHARGER001",
        name=fake.word().capitalize() + " Charger for iPhone",
        description=fake.sentence(),
        category=accessories_category,
    )
    create_product(
        code="SAM_CHARGER001",
        name=fake.word().capitalize() + " Charger for Samsung Galaxy",
        description=fake.sentence(),
        category=accessories_category,
    )

    # Create earphones for mobile phones
    create_product(
        code="IPH_EARPHONES001",
        name=fake.word().capitalize() + " Earphones for iPhone",
        description=fake.sentence(),
        category=accessories_category,
    )
    create_product(
        code="SAM_EARPHONES001",
        name=fake.word().capitalize() + " Earphones for Samsung Galaxy",
        description=fake.sentence(),
        category=accessories_category,
    )

    print("Product and Specification data has been populated successfully.")
