from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from triangle import views

urlpatterns = [
    path('triangle/', views.TriangleList.as_view()),
    path('triangle/<int:pk>/perimeter', views.TriangleDetail.as_view()),
    path('triangle/<int:pk>/area', views.TriangleDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)