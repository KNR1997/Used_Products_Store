# Generated by Django 5.0.1 on 2024-01-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('copies', models.IntegerField()),
                ('copies_available', models.IntegerField()),
                ('category', models.CharField(max_length=45)),
                ('img', models.BinaryField()),
            ],
        ),
    ]
