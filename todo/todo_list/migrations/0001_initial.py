# Generated by Django 3.0.3 on 2020-02-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('due_date', models.DateTimeField(verbose_name='due date')),
            ],
        ),
    ]
