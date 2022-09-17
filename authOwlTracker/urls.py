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
#  recordar  configurar  estos  path  @ felipe < @ldordelly

  from django.contrib import admin
  from django.urls import path
  
  from appOwlTracker.models.account.create import create_account
  from appOwlTracker.models.bank_accounts.create import create_bank_accounts
  from appOwlTracker.models.data_log.create import create_data_log
  from appOwlTracker.models.section_categories.create import create_section
  


urlpatterns = [

    path('admin/', admin.site.urls),
    path("account/", create_account),
    path("center_bank_accounts/",create_bank_accounts),
    path(" registries/", create_data_log),
    path("sections categories/", create_section), 
    
    
    
    
    
]
