# Generated by Django 2.2 on 2019-06-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='Remark',
            field=models.TextField(blank=True),
        ),
    ]
