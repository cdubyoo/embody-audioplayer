# Generated by Django 3.2.7 on 2021-09-06 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='audio.audio'),
        ),
    ]
