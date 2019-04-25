from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from square import views

urlpatterns = [
    path('square/', views.SquareList.as_view()),
    path('square/<int:pk>/perimeter', views.SquareDetail.as_view()),
    path('square/<int:pk>/area', views.SquareDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)