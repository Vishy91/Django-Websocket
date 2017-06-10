
from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^$', views.display, name='display'),
    url(r'^update/', views.update, name='update'),
    url(r'^main/', views.display, name='display'),
]
