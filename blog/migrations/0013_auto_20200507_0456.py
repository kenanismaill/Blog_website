# Generated by Django 3.0.3 on 2020-05-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200506_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[(' New', 'New'), ('True', 'True'), ('False', 'False ')], default='New', max_length=10),
        ),
    ]
