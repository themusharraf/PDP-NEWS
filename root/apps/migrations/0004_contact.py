# Generated by Django 5.0.4 on 2024-05-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
