from django.db import models

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"), 
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    
    name = models.CharField(max_length=60)
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default="FR"
    )
    
    def __str__(self):
        return self.name
    
    def is_upperclass(self):
        return self.year_in_school in ['JR', 'SR']
    
    class Meta:
        verbose_name = "Student" 
        verbose_name_plural = "Students"
        ordering = ['name']