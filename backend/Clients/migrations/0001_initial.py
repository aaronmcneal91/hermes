# Generated by Django 4.2.3 on 2023-07-21 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client_Type', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_Type.client_type')),
            ],
        ),
    ]
