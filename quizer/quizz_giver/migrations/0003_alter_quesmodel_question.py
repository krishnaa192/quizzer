# Generated by Django 4.0.6 on 2022-07-17 11:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz_giver', '0002_alter_quizes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='question',
            field=ckeditor.fields.RichTextField(default='None'),
        ),
    ]