# Generated by Django 3.2.25 on 2025-05-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=255)),
                ('service_date', models.DateTimeField()),
                ('summary', models.TextField()),
                ('entry_date', models.DateField()),
                ('exit_date', models.DateField()),
            ],
        ),
    ]
