# Generated by Django 3.1.1 on 2021-11-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default='useravatar.png', upload_to='profilepic'),
        ),
    ]
