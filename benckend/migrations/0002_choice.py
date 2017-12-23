# Generated by Django 2.0 on 2017-12-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benckend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='选项')),
                ('votes', models.IntegerField(default=0, verbose_name='投票数')),
            ],
        ),
    ]
