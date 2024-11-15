from datetime import datetime

from django.shortcuts import render


# Create your views here.
def home_page(request):
    contex = {
        "current_time": datetime.now(),
        "person": {
            "name": "Dimo",
            "last_name": "Ivanov",
            "email": "dimo.ivanov.lex@gmail.com",
        }
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
