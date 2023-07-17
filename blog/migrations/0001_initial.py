# Generated by Django 4.2 on 2023-06-22 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.category')),
            ],
        ),
    ]
