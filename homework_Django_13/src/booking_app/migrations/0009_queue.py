# Generated by Django 5.0.4 on 2024-06-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0008_rename_queue_personqueue_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
