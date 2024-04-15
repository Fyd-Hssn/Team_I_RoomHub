# Generated by Django 5.0.2 on 2024-04-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_listing_alter_favorite_listing_delete_roomlisting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name="listing",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]