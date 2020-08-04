from django.conf.urls import url
from django.urls import path

from welcome import views

urlpatterns = [
    path('', views.index),
    path('team/', views.team),
    path('upload/', views.uploadfilepage),
    path('upload_file', views.upload_file),
    path('personal', views.personal),
    path('index/', views.index)
]
