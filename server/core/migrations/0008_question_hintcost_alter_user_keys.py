# Generated by Django 4.0.5 on 2022-10-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_question_img2_alter_question_img3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hintCost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='keys',
            field=models.PositiveIntegerField(default=2),
        ),
    ]