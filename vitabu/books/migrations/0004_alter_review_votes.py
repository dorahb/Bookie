# Generated by Django 4.1 on 2022-08-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='votes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
