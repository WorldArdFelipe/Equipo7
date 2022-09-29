"""authOwlTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appOwlTracker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('dashboard/', admin.site.urls),
    #path('seguimiento/', admin.site.urls),
    
    # Default 
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    
    
    # Url crear usuario o , [POST]
    path('create_user/',views.UserView.as_view()),
        
    # Url [GET],[PUT],[DELETE]
    path('user/<int:id>',views.UserView.as_view()),
    
    # Url consulta todos los usuarios
    path('all_user/',views.AllUserView.as_view()),
    
    
    # Url add Bank [POST]
    path('create_bank/',views.BankAccountView.as_view()),
    
    
    
    path('create_movements/',views.MovementsRecordedView.as_view()),
    path('movements/<int:id_user>',views.MovementsRecordedView.as_view()),
]
