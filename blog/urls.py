from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),# 실 url , 참조할 view 함수, 참조되어지는 이름
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new', views.post_new, name = 'post_new'),
    path('post/edit/<int:pk>/',views.post_edit, name = "post_edit")
]