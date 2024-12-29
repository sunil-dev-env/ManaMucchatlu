from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('create-thread/', views.create_thread, name='create_thread'),
    path('nickname/', views.set_nickname, name='nickname'),
]
