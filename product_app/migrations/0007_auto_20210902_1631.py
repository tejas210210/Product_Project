# Generated by Django 2.2.7 on 2021-09-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_auto_20210901_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user_token',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
