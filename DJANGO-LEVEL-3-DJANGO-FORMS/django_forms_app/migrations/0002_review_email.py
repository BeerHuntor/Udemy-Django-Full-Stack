# Generated by Django 5.0.4 on 2024-04-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_forms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
