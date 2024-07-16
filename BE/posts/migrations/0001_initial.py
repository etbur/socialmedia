# Generated by Django 5.0.7 on 2024-07-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('audience', models.CharField(default='public', max_length=20)),
            ],
        ),
    ]
