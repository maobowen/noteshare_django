# Generated by Django 2.0 on 2017-12-29 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Country ID')),
                ('name', models.CharField(max_length=100, verbose_name='Country Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Course ID')),
                ('number', models.CharField(max_length=20, verbose_name='Course Number')),
                ('name', models.CharField(max_length=100, verbose_name='Course Name')),
                ('subject', models.CharField(max_length=10, verbose_name='Course Subject')),
                ('fontawesome', models.CharField(default='book', max_length=50, verbose_name='Font Awesome')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='University ID')),
                ('name', models.CharField(max_length=100, verbose_name='University Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noteshare.Country', verbose_name='Country')),
            ],
            options={
                'ordering': ['country', 'name'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noteshare.University', verbose_name='University'),
        ),
    ]