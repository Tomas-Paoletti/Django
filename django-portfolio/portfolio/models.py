from distutils.command.upload import upload
from distutils.file_util import move_file
from optparse import TitledHelpFormatter
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=300)
    image = ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)
