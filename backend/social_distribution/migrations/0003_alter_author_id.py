# Generated by Django 4.1.7 on 2023-03-01 01:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('social_distribution', '0002_alter_followers_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]