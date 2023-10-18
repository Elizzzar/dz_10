from django.urls import path
from app.views import *
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', TaskListView.as_view(), name='task_list'),
    re_path(r'^create$', TaskCreateView.as_view(), name='task_create'),
    re_path(r'^(?P<pk>\d+)/$' ,TaskDetailView.as_view(), name='task_detail'),
    re_path(r'^(?P<pk>\d+)/update$' ,TaskUpdateView.as_view(), name='task_update'),
    re_path(r'^(?P<pk>\d+)/delete$' ,TaskDeleteView.as_view(), name='task_delete'),
]
