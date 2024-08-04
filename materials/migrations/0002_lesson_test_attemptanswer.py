# Generated by Django 5.0.7 on 2024-08-04 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название урока', max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('course', models.ForeignKey(help_text='Укажите курс', on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='materials.course', verbose_name='Курс')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название теста', max_length=150, verbose_name='Название')),
                ('description', models.TextField(help_text='Укажите Описание вопроса', verbose_name='Описание вопроса')),
                ('correct_answer', models.TextField(help_text='Укажите Правильный ответ', verbose_name='Правильный ответ')),
                ('lesson', models.ForeignKey(help_text='Укажите урок', on_delete=django.db.models.deletion.CASCADE, related_name='test', to='materials.lesson', verbose_name='Курс')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='AttemptAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(help_text='Укажите ваш ответ', verbose_name='Попытка ответа')),
                ('answer_bool', models.BooleanField(blank=True, null=True, verbose_name='Правильно/Неправильно')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
                ('test', models.ForeignKey(help_text='Укажите тест', on_delete=django.db.models.deletion.CASCADE, related_name='attempt_answer', to='materials.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Попытка ответа',
                'verbose_name_plural': 'Попытки ответа',
            },
        ),
    ]
