from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    descriptive_title = models.CharField(max_length=64, unique=True)
    course_number = models.CharField(max_length=32, unique=True)
    lecture_hours = models.IntegerField()
    laboratory_hours = models.IntegerField()
    units = models.IntegerField()

    def __str__(self):
        return self.course_number
