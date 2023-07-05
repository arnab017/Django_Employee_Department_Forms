"""
URL configuration for Emp_Dept project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('insert_Dept_Form/',insert_Dept_Form,name='insert_Dept_Form'),
    path('insert_Emp_Form/',insert_Emp_Form,name='insert_Emp_Form'),
    
    path('retrieve_Dept/',retrieve_Dept,name='retrieve_Dept'),
    path('retrieve_Emp/',retrieve_Emp,name='retrieve_Emp'),
    
    path('dept_checkbox/',dept_checkbox,name='dept_checkbox'),
    path('emp_checkbox/',emp_checkbox,name='emp_checkbox'),
]
