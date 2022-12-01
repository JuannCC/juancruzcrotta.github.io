from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_posts(request):
    posts= Post.objects.all()
    return render(request,"posts.html", {'posts':posts})

def post_detail(request, post_id):
    #Le pasamos el primary key que es el ID de la publicacion, entonces si no existe el blog nos tira el error
    post= get_object_or_404(Post, pk=post_id)
    return render(request,"post_detail.html", {'post':post})