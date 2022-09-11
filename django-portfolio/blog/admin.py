from django.contrib import admin
from .models import Post  # importa los modelos de models.py

# Register your models here.

admin.site.register(Post)
# hacer primero pyrhon manage.py makemigratios y luego
# python manage.py migrate para subir modelos
