# Generated by Django 5.0.7 on 2024-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_alter_snippet_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('js', 'JavaScript'), ('cpp', 'C++'), ('HTML', 'html'), ('py', 'Python')], max_length=30),
        ),
    ]
