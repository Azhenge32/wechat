from django.db import models


class Question(models.Model):
    question_text = models.CharField(verbose_name="问题", max_length=200)
    pub_date = models.DateTimeField(verbose_name="发布日期")


#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(verbose_name="选项", max_length=200)
#    votes = models.IntegerField(verbose_name="投票数", default=0)