from django.db import models
from department.models import Department

CHOICE = [
    ('HOD', 'Head of Department'),
    ('CT', 'Class Teacher'),
    ('AST', 'Assistant'),
]

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_role = models.CharField(max_length=3, choices=CHOICE)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.staff_name} : {self.department.dep_name} - [{self.staff_role}]"