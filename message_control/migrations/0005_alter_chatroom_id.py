# Generated by Django 4.2 on 2023-05-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_control', '0004_rename_profile_matchex_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
