from django.db import models

class Calendar(models.Model):
    period = models.IntegerField()
    class_title = models.CharField(max_length=256)
    teacher_name = models.CharField(max_length=256)
    cal_id = models.CharField(max_length=256, unique=True)


    def __unicode__(self):
        return self.class_title + ' ' + self.teacher_name + ' ' + str(self.period)
