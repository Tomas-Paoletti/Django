from django.contrib import admin
from django.urls import path, include  # include permite leer las carpetas
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import home
from blog import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path(
        "blog/", include("blog.urls")
    ),  # aca el include lo que nos hace es usar urlspy de blog para cargar las rutas de blog
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
