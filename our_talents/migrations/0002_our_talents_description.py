# Generated by Django 2.1.7 on 2019-02-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_talents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_talents',
            name='description',
            field=models.TextField(default=''),
        ),
    ]