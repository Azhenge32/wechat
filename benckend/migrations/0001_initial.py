# Generated by Django 2.0 on 2017-12-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='问题')),
                ('pub_date', models.DateTimeField(verbose_name='发布日期')),
            ],
        ),
    ]
