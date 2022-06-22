# Generated by Django 3.1.3 on 2022-04-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('companyName', models.CharField(db_column='company_name', max_length=100, null=True)),
                ('email', models.CharField(db_column='email', max_length=100, null=True)),
                ('active', models.BooleanField(default=False)),
                ('description', models.TextField(db_column='description', max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Clientes',
                'db_table': 'customer',
            },
        ),
    ]
