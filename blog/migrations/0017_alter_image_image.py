# Generated by Django 3.2.5 on 2021-09-14 07:15

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210914_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default='default', upload_to='images/', verbose_name='Image'),
        ),
    ]
