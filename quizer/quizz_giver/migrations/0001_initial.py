# Generated by Django 4.0.6 on 2022-07-17 03:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.IntegerField(blank=True, help_text='Duration of quiz in minutes', null=True)),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('require_score', models.IntegerField(blank=True, help_text=' require score in %', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_score', models.IntegerField()),
                ('percent', models.CharField(max_length=200)),
                ('names_quizer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', ckeditor.fields.RichTextField()),
                ('option1', ckeditor.fields.RichTextField()),
                ('option2', ckeditor.fields.RichTextField()),
                ('option3', ckeditor.fields.RichTextField()),
                ('option4', ckeditor.fields.RichTextField()),
                ('ans', ckeditor.fields.RichTextField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], max_length=12)),
                ('quiz_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz_giver.quizes')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('Bio', models.TextField(blank=True, null=True)),
                ('tel', models.CharField(default='', max_length=20)),
                ('work', models.TextField(default='')),
                ('designation', models.CharField(default='None', max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'others')], default='', max_length=22)),
                ('Address', models.TextField(default='None')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]