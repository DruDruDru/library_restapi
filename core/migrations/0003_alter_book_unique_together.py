# Generated by Django 4.2.7 on 2023-11-20 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('publisher', 'author')},
        ),
    ]
