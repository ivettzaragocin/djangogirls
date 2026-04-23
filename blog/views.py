from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Aquí obtenemos los posts de la base de datos
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Es VITAL que el diccionario {'posts': posts} esté al final
    return render(request, 'blog/post_list.html', {'posts': posts})