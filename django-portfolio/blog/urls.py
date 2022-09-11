from turtle import pos
from django.urls import path
from .views import post, post_detail

app_name = "blog"  # atajo para hacer
urlpatterns = [
    path("", post, name="post"),
    path(
        "<int:post_id>", post_detail, name="post_detail"
    ),  # lo que esta en <> es lo que va a buscar en la url como id
]
