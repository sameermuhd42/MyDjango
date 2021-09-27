from django.db import models
from reporting.models import Batch, Course

# Create your models here.


class TimeSheet(models.Model):
    user = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    options = (('in progress', 'in progress'), ('completed', 'completed'))
    topic_status = models.CharField(max_length=255, choices=options, default='in progress')

    def __str__(self):
        return self.topic


