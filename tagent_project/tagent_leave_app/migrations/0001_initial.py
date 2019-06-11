# Generated by Django 2.2.2 on 2019-06-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_number', models.CharField(default=None, max_length=20)),
                ('phone_number', models.IntegerField(default=None)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
                ('days_of_leave', models.IntegerField(default=None)),
                ('status', models.BooleanField(default=False)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagent_leave_app.Employee')),
            ],
        ),
    ]
