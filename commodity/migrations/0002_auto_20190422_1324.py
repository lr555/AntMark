# Generated by Django 2.1.4 on 2019-04-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='image',
            field=models.ImageField(default='static/img/defaultIcon.jpg', upload_to='images/%Y/%m/%d'),
        ),
    ]