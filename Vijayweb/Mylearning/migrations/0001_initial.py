# Generated by Django 2.1.2 on 2019-05-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview_QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('question_num', models.IntegerField()),
                ('question_des', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=2000)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'interview_QA',
            },
        ),
        migrations.CreateModel(
            name='Reading_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='document/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reading_material',
            },
        ),
    ]
