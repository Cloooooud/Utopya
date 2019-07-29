from django.db import models
 
class Test(models.Model):
    SID = models.IntegerField()
    name = models.CharField(max_length=20)
    test = models.CharField(max_length=40)
    score_chinese =  models.IntegerField()
    score_math = models.IntegerField()
    score_English = models.IntegerField()
    score_physics = models.IntegerField()
    score_chemisty = models.IntegerField()

