# """DiabetesPrediction URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from . import views
# admin.site.site_header = 'Diabetes prediction'
# admin.site.index_title = ' Admin  Administration'


# urlspatterns = [
  
#     path ("",views.index,name='index'),
#     path("home",views.home),
#     path ("predict/",views.predict,name='predict'),
#     path ("predict/result",views.result),
#     path ("login",views.login,name='login'),
#     path ("login/predict",views.predict),
#     path ("register",views.register,name='register'),
#     path ("Result",views.Result,name='Result'),
#     path ("password",views.password,name='password'),
   
# ]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path ("index",views.index,name='index'),
    path ("home",views.home),
    path ("predict/",views.predict,name='predict'),
    path ("predict/result",views.result),
    path ("login",views.login,name='login'),
    path ("login/predict",views.predict),
    path ("register",views.register,name='register'),
    path ("Result",views.Result,name='Result'),
     path ("password",views.password,name='password'),
    
]
