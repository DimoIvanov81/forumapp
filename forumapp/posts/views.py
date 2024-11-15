from datetime import datetime

from django.shortcuts import render

from forumapp.forms import PersonForm


# Create your views here.
def home_page(request):
    contex = {
        "form": PersonForm(),
    }
    return render(request, 'home_page.html', contex)


def posts(request):
    contex = {
        'posts': [
            {"title": "How to create posts",
             "author": "Dimo",
             "content": "I really like this post.",
             "created_time": datetime.now()},
            {"title": "How to keep things up",
             "author": "Dimo Ivanov",
             "content": "I really want to be more successful",
             "created_time": datetime.now()},

            {"title": "How to be like me",
             "author": "Eva Tarneva",
             "content": "I am go for it.",
             "created_time": datetime.now()}
        ]

    }
    return render(request, 'posts/posts.html', contex)
