# Generated by Django 4.1.7 on 2023-02-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_distribution', '0002_rename_auther_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='auther',
        ),
        migrations.RemoveField(
            model_name='post',
            name='commentSrc',
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
