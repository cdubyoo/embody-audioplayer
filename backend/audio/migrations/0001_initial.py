# Generated by Django 3.2.7 on 2021-09-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
