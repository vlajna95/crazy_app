# Generated by Django 3.1 on 2020-08-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ManyToManyField(related_name='answers', to='quiz.Question'),
        ),
    ]
