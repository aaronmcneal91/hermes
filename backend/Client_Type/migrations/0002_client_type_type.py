# Generated by Django 4.2.3 on 2023-07-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_Type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_type',
            name='type',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]