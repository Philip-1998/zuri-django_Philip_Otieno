# Generated by Django 3.2.5 on 2022-05-31 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20220531_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='text',
            new_name='choice_text',
        ),
    ]
