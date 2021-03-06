# Generated by Django 2.0.2 on 2018-03-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('has_math', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, default=1.0, max_digits=4)),
                ('input_file', models.FileField(upload_to='')),
                ('output_file', models.FileField(upload_to='')),
                ('secret', models.BooleanField(default=False)),
                ('mandatory', models.BooleanField(default=False)),
                ('show_errors', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'verbose_name_plural': 'syllabuses'},
        ),
    ]
