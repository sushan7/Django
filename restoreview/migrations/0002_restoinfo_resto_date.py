# Generated by Django 2.1.7 on 2019-04-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoreview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restoinfo',
            name='resto_date',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
