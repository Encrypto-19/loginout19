# Generated by Django 3.0.4 on 2020-04-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logio', '0003_content_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='article_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
