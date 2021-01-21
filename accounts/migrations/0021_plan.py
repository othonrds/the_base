# Generated by Django 3.0 on 2021-01-09 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_delete_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200, null=True)),
                ('recurrence', models.CharField(choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Anually', 'Anually')], max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer')),
            ],
        ),
    ]