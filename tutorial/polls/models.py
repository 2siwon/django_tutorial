from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return "설문조사 : {}".format(self.title)


class Choice(models.Model):
    question = models.ForeignKey('Question')
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "설문조사의 제목 : {}, 선택지 {}".format(self.question, self.title)
