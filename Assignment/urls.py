"""Assignment URL Configuration

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
from django.urls import path
from india.views import *
from dhoni.views import *
from virat.views import *
from rohit.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('india',india,name='india'),
    path('dhoni/',dhoni,name='dhoni'),
    path('virat/',virat,name='virat'),
    path('rohit/',rohit,name='rohit'),
]
