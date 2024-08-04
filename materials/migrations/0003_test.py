# Generated by Django 5.0.7 on 2024-08-03 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_lesson'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название теста', max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Укажите Описание вопроса', null=True, verbose_name='Описание вопроса')),
                ('correct_answer', models.TextField(blank=True, help_text='Укажите Правильный ответ', null=True, verbose_name='Правильный ответ')),
                ('lesson', models.ForeignKey(blank=True, help_text='Укажите урок', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='materials.lesson', verbose_name='Курс')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
        ),
    ]
