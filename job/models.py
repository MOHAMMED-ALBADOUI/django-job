from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)


class Job (models.Model): # this class Equivalent table in db
    title = models.CharField(max_length=100) # Column
    jop_type = models.CharField(max_length=10 , choices=JOB_TYPE) # column
    descirption = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacnancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title