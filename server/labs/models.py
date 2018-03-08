from django.db import models


# Create your models here.
class Syllabus(models.Model):
    class Meta:
        verbose_name_plural = "syllabuses"

    year_introduced = models.IntegerField()
    active = models.BooleanField()
    name = models.CharField(max_length=32)


class Subject(models.Model):
    syllabus = models.ForeignKey(to=Syllabus, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=32)
    name = models.CharField(max_length=48)


class Lab(models.Model):
    semester = models.IntegerField()
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)


class Question(models.Model):
    content = models.CharField(max_length=5000)
    has_math = models.BooleanField()


class TestCase(models.Model):
    weight = models.DecimalField(decimal_places=3, max_digits=4, default=1.0)
    input_file = models.FileField()
    output_file = models.FileField()
    secret = models.BooleanField(default=False)
    mandatory = models.BooleanField(default=False)
    show_errors = models.BooleanField(default=True)
