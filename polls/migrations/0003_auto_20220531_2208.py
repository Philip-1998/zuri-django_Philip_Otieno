# Generated by Django 3.2.5 on 2022-05-31 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_choice_question_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_text',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
    ]