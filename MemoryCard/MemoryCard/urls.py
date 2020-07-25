"""MemoryCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from memoryCardApp.views import (CreateMemory,
                                 Memory_view,
                                 MemoryDelete_view,
                                 MemoryEdit_view
                                 )


urlpatterns = [ 
    path('',CreateMemory.as_view(), name = 'CreateMemory'),
    path('list/',Memory_view.as_view(), name = 'Memory_view'),
    path('<int:pk>/delete', MemoryDelete_view.as_view(), name = 'MemoryDelete_view'),
    path('<int:id>/update', MemoryEdit_view.as_view(), name = 'MemoryEdit_view'),
    path('admin/', admin.site.urls), 
]
