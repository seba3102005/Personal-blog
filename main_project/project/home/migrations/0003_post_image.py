# Generated by Django 5.1.4 on 2024-12-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%y/%m/%d'),
        ),
    ]
