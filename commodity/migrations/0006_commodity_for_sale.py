# Generated by Django 2.1.4 on 2019-04-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0005_auto_20190413_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
