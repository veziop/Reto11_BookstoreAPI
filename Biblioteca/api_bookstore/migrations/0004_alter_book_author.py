# Generated by Django 4.0.1 on 2022-01-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0003_rename_added_by_author_added_by_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api_bookstore.author'),
        ),
    ]