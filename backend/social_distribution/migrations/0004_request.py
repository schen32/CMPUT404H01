# Generated by Django 4.1.7 on 2023-03-03 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_distribution', '0003_post_authorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='social_distribution.author')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object', to='social_distribution.author')),
            ],
        ),
    ]
