# Generated by Django 4.2.2 on 2023-07-05 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=30)),
                ('loc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=30)),
                ('sal', models.IntegerField()),
                ('hire_date', models.DateField()),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]