# Generated by Django 3.0.3 on 2020-06-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200601_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
