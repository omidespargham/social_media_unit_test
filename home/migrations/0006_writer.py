# Generated by Django 4.1.4 on 2023-04-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]