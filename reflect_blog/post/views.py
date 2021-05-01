from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home_page(request):
    if(request.GET != {}):
        search = dict(request.GET)
        search_list = list(search.items())
        query_search = search_list[0][0]
        query_item = search_list[0][1][0]
        if query_search == "filter_by":
            if(query_item == "Tech" or "Motivation" or "Lifestyle" or "School Life"):
                category = Category.objects.get(name=query_item)
                return render(request, 'index.html', {'title': "Reflect Blog", 'posts': category.post_set.all()})

        elif query_search == "query":
            return render(request, 'index.html', {'title': "Reflect Blog", 'posts': Post.objects.filter(title__contains=query_item)})
        return render(request, 'index.html')
    return render(request, 'index.html', {'title': "Reflect Blog", 'posts': Post.objects.order_by('-timestamp').all()})

def post_page(request, slug_text):
    post = Post.objects.filter(slug=slug_text)
    if post.exists():
        post = post.first()
    else:
        post = HttpResponseNotFound("Page Not Found")
    return render(request, 'post.html', {'title': post.title, "post": post})

def author_page(request):
    return render(request, 'author.html', {'title': "About | Content Creator"})

