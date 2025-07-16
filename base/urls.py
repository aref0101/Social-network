from django.urls import path
from .import views

urlpatterns= [
    path('', views.home, name= 'home'),
    path('addpost/', views.addpost, name= 'addpost'),
    path('loginuser/', views.loginuser, name= 'loginuser'),
    path('logoutuser/', views.logoutuser, name= 'logoutuser'),
    path('registeruser/', views.registeruser, name= 'registeruser'),
    path('editpost/<str:pk>/', views.editpost, name= 'editpost'),
    path('deletepost/<str:pk>/', views.deletepost, name= 'deletepost'),
    path('userpage/<str:pk>/', views.userpage, name= 'userpage'),
    path('edituser/', views.edituser, name= 'edituser'),
    path('comment/<str:pk>/', views.comment, name= 'comment'),
    path('toggleLike/<str:pk>/', views.toggleLike, name= 'toggleLike'),
    path('deletecomment/<str:pk>/', views.deletecomment, name= 'deletecomment'),
]