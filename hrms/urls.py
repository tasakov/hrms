"""
URL configuration for hrms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
import employees.views
from django.conf.urls import include
import empPerformance.views
from django.contrib import admin
from django.urls import path, include

from accounts import views
from hrms import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',include('employees.urls')),
    path('performance/',include('empPerformance.urls')),
    path('tasks/',include('tasks.urls')),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('documents/', include('documents.urls')),
    path('employees/',include('employees.urls')),
    path('clients/',include('clients.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# =======
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# import employees.views
# from django.conf.urls import include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('employees/',include('employees.urls'))
# ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# >>>>>>> upstream/master
