#@blair the view template responsible for displaying our action
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
# return HttpResponse('Hello I am Blair. Some Say I am a good programmer.')

 posts= Posts.objects.all()[:10]

 context = {
	'title' : 'Latest Posts by Blair',
	'posts' : posts
	}
 return render(request, 'posts/index.html', context)
 
#create a function for details
def details(request,id):
 posts = Posts.objects.get(id=id)
 
 context= {
	'posts': posts
	}
 return render(request, 'posts/details.html', context)
	