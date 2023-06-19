from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('login/', views.login_view, name='user_login'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('logout/', views.logout, name='user_logout'),
]
