from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='noteshare_index'),
    re_path(r'^([a-zA-Z\-]+)/$', views.university, name='noteshare_university'),
    re_path(r'^([a-zA-Z\-]+)/([0-9a-zA-Z\-]+)/$', views.course, name='noteshare_course'),
]
