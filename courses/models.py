from django.db import models


class Course(models.Model):
            name = models.CharField(max_length=100, null=True)
            instrutor_name = models.CharField(max_length=100, null=True)
            description = models.TextField(null=True)
            start_date = models.DateField(null=True)
            end_date = models.DateField(null=True)
            student_num = models.IntegerField(null=True)