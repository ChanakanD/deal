# Generated by Django 4.2 on 2023-05-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('no_case', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='img')),
                ('lastLogin', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(max_length=10)),
                ('group', models.CharField(max_length=10)),
            ],
        ),
    ]
