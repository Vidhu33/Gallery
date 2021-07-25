from django.urls import path
from . import views

urlpatterns = [
    # url to home page
    path('home/',views.gallery, name="gallery"),
    # url to add image page
    path('addImage/',views.addImage, name="addImage"),
    # url to view image page
    path('image/<str:pk>/',views.image, name="image"),
]