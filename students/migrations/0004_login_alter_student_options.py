# Generated by Django 4.2.1 on 2023-05-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Students Name'},
        ),
    ]
