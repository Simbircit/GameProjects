from django.contrib.auth.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='GameProjects'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('add_game/', views.add_game, name='add_game'),
    path('profile/', views.profile, name='profile'),
    path('<genre_name>', views.main_genre, name='GameProjects'),
    path('game/<game_id>/', views.game_page, name='game'),
    path('delete_image/<image_id>/', views.delete_image, name='delete_image'),
    path('delete_file/<file_id>/', views.delete_file, name='delete_file'),

]
