# Generated by Django 2.1.2 on 2018-11-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('context', models.TextField(verbose_name='Описание')),
                ('datetime', models.DateTimeField(verbose_name='Дата публикации')),
                ('pic', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
        ),
    ]