from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Lab, Syllabus, Subject, Question, TestCase])