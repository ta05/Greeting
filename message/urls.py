from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'message'
urlpatterns = [
    path('all', views.all, name="all"),
    path('', views.index, name="index"),
    url(r'^(?P<message_id>[0-9]+)/delete_message/$', views.deleteMessage, name="delete_message")
]