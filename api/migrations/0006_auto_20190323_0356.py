# Generated by Django 2.1.7 on 2019-03-23 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190323_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='User',
            new_name='user',
        ),
    ]
