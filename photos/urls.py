from django.urls import path
from . import views

urlpatterns = [

    path("", views.gallery, name = 'gallery'),

    path("photos/<int:pk>/", views.viewPhoto, name = 'photos' ),

    path('add/', views.addPhoto, name='add'),
]