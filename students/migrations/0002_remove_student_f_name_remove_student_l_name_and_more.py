# Generated by Django 4.2.1 on 2023-05-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='l_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobile',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='mmm adress', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default='22'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='mmmm@mmm.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
