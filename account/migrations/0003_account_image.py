# Generated by Django 3.1.1 on 2021-11-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_is_ranger'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profilepic'),
        ),
    ]
