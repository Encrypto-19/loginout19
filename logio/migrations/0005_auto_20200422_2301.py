# Generated by Django 3.0.4 on 2020-04-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logio', '0004_content_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
