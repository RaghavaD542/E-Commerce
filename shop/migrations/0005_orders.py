# Generated by Django 5.0.1 on 2024-02-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_alter_product_category_alter_product_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
