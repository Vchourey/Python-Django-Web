# Generated by Django 2.1.2 on 2019-06-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mylearning', '0006_auto_20190621_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_form',
            name='EmailStu',
        ),
        migrations.RemoveField(
            model_name='reg_form',
            name='TextArea',
        ),
    ]