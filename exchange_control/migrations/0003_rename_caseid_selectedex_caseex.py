# Generated by Django 4.2 on 2023-05-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_control', '0002_selectedex_user_alter_selectedex_caseid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selectedex',
            old_name='caseId',
            new_name='caseEx',
        ),
    ]