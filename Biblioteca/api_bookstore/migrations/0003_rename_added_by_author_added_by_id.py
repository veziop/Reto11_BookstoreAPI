# Generated by Django 4.0.1 on 2022-01-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0002_alter_author_created_date_alter_book_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='added_by',
            new_name='added_by_id',
        ),
    ]
