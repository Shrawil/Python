from django.db import models
from department.models import Department

CHOICE = [
    (1, 'First Year'),
    (2, 'Second Year'),
    (3, 'Third Year'),
]

class Students(models.Model):
    student_name = models.CharField(max_length=30)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_year = models.IntegerField(choices=CHOICE)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    def __str__(self):
        year = self.student_year
        if year == 1: 
            yr = 'st'
        elif year == 2:
            yr = 'nd'
        elif year == 3:
            yr = 'rd'
        return f"{self.student_name} | {self.department.dep_name} {year}{yr} Year"