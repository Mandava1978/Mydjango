from django.urls import path 
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name="ïndex"),
    path('about/', views.myfunctionabout, name="about"),
   # path('add/<int:a>/<int:b>/', views.add, name="add"),
    path('intro/<str:name>/<int:age>/', views.intro, name="intro"),
    path('add/<int:a>/<int:b>/', views.add, name="add"),
]

