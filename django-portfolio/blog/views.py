from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post(request):
    post = Post.objects.all()
    return render(request, "post.html", {"post": post})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post, pk=post_id
    )  # primer valor es modelo y segundo lo que se quiere buscar en este caso id

    return render(request, "post_detail.html", {"post": post})
