# Generated by Django 4.2.8 on 2025-06-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_librarian_password_alter_librarian_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='password',
            field=models.CharField(default='temp_password', max_length=128),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='username',
            field=models.CharField(default='temp_username', max_length=150, unique=True),
        ),
    ]
