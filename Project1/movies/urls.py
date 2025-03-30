from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('movies/', views.movies, name='movies'),
    path('create_list/', views.create_list, name='create_list'),
    path('add_to_list/<int:movie_id>/', views.add_to_list, name='add_to_list'),
    path('add_to_list/<int:movie_id>/<int:list_id>/', views.add_to_specific_list, name='add_to_specific_list'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete_list'),
    path('view_list/<int:list_id>/', views.view_list, name='view_list'),
    path('remove_from_list/<int:list_id>/<int:movie_id>/', views.remove_from_list, name='remove_from_list'),
    path('movie/<int:movie_id>/comments/', views.movie_comments, name='movie_comments'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('movie/<int:movie_id>/rate/', views.rate_movie, name='rate_movie'),
    path('movie/<int:movie_id>/ratings/', views.view_ratings, name='view_ratings'),
] 