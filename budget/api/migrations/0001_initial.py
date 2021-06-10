# Generated by Django 3.2.4 on 2021-06-09 11:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
                ('name', models.TextField(max_length=2000, verbose_name='Полное наименование')),
                ('startdate', models.DateTimeField(default=datetime.datetime.today, verbose_name='Дата начала действия записи')),
                ('enddate', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания действия записи')),
                ('status', models.CharField(choices=[('ACTIVE', 'Актуальная запись'), ('ARCHIVE', 'Архивная запись')], default='ACTIVE', max_length=7, verbose_name='Статус записи')),
                ('budgettype', models.CharField(choices=[(None, '(Unknown)'), ('00', 'Прочие бюджеты'), ('01', 'Федеральный бюджет'), ('02', 'Бюджет субъекта РФ'), ('03', 'Бюджеты внутригородских МО г. Москвы и г. Санкт-Петербурга'), ('04', 'Бюджет городского округа'), ('05', 'Бюджет муниципального района'), ('06', 'Бюджет Пенсионного фонда РФ'), ('07', 'Бюджет ФСС РФ'), ('08', 'Бюджет ФФОМС'), ('09', 'Бюджет ТФОМС'), ('10', 'Бюджет поселения'), ('98', 'Распределяемый доход'), ('99', 'Доход организации (только для ПДИ)')], default='00', max_length=2, verbose_name='Тип бюджета')),
                ('parentcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.budget', verbose_name='Вышестоящий бюджет')),
            ],
            options={
                'verbose_name': 'Справочник бюджетов',
                'verbose_name_plural': 'Справочники бюджетов',
            },
        ),
        migrations.CreateModel(
            name='GlavBudgetClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, verbose_name='Код')),
                ('name', models.TextField(blank=True, max_length=254, null=True, verbose_name='Сокращенное наименование')),
                ('startdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата начала действия записи')),
                ('enddate', models.DateTimeField(null=True, verbose_name='Дата окончания действия записи')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.budget', verbose_name='Бюджет')),
            ],
            options={
                'verbose_name': 'Справочник главы по бюджетной классификации',
                'verbose_name_plural': 'Справочники главы по бюджетной классификации',
            },
        ),
    ]
