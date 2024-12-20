# Generated by Django 4.2.16 on 2024-11-09 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at_todo_description_todo_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.CharField(max_length=255, unique=True)),
                ('list_name', models.CharField(max_length=255)),
                ('is_default', models.BooleanField(default=False)),
                ('is_display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField()),
                ('comment', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo.list')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
