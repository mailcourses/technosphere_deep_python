from django.db import models

class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=128, null=False)
    descr = models.TextField('Описание фильма', null=True)
    year = models.IntegerField('Год выхода', null=True)
