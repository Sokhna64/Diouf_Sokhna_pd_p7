# Generated by Django 4.0.1 on 2022-01-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_article_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='miniature',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]