#@blair the url template responsible for calling the view
#index is the method that we have in views.py
from django.conf.urls import url
from . import views 

urlpatterns = [
   url(r'^$', views.index, name='index') ,
   url(r'^details/(?P<id>\d+)/$', views.details, name='details') 
	 ];
