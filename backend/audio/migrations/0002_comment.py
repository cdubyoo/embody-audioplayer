# Generated by Django 3.2.7 on 2021-09-05 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16)),
                ('body', models.TextField()),
                ('timestamp_minutes', models.CharField(max_length=2)),
                ('timestamp_seconds', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.audio')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
