# Generated by Django 3.1.3 on 2022-04-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('items', models.ManyToManyField(to='item.Item')),
            ],
            options={
                'verbose_name': 'Templ ates',
                'verbose_name_plural': 'Assessment Templates',
                'db_table': 'template',
            },
        ),
    ]
