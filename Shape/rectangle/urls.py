from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rectangle import views

urlpatterns = [
    path('rectangle/', views.RectangleList.as_view()),
    path('rectangle/<int:pk>/perimeter', views.RectangleDetail.as_view()),
    path('rectangle/<int:pk>/area', views.RectangleDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)