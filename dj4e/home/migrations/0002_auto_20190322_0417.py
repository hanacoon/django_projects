# Generated by Django 2.1.7 on 2019-03-22 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='ISO',
        ),
        migrations.RemoveField(
            model_name='site',
            name='category',
        ),
        migrations.RemoveField(
            model_name='site',
            name='region',
        ),
        migrations.RemoveField(
            model_name='site',
            name='states',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ISO',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
        migrations.DeleteModel(
            name='States',
        ),
    ]
