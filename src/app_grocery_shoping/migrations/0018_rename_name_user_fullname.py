# Generated by Django 4.1.7 on 2023-03-29 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0017_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='fullname',
        ),
    ]
