# Generated by Django 4.0.5 on 2023-05-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_answerhistory_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerhistory',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
