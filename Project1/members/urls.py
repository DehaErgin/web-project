from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('<str:username>/', views.member_detail, name='member_detail'),
    path('<str:username>/reviews/', views.member_reviews, name='member_reviews'),
] 