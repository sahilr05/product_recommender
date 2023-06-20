# Generated by Django 4.2.2 on 2023-06-20 07:18
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_product_frequently_bought_together_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="created_datetime",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="deleted_datetime",
            new_name="deleted_at",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="modified_datetime",
            new_name="modified_at",
        ),
        migrations.RenameField(
            model_name="orderproduct",
            old_name="created_datetime",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="orderproduct",
            old_name="deleted_datetime",
            new_name="deleted_at",
        ),
        migrations.RenameField(
            model_name="orderproduct",
            old_name="modified_datetime",
            new_name="modified_at",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="created_datetime",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="deleted_datetime",
            new_name="deleted_at",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="modified_datetime",
            new_name="modified_at",
        ),
        migrations.RenameField(
            model_name="specification",
            old_name="created_datetime",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="specification",
            old_name="deleted_datetime",
            new_name="deleted_at",
        ),
        migrations.RenameField(
            model_name="specification",
            old_name="modified_datetime",
            new_name="modified_at",
        ),
        migrations.AlterField(
            model_name="product",
            name="frequently_bought_together",
            field=models.ManyToManyField(to="api.product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="similar_products",
            field=models.ManyToManyField(to="api.product"),
        ),
    ]