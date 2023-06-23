"""
URL configuration for project29 project.

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
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('FUNCTION_BASED_VIEW/',FUNCTION_BASED_VIEW,name='FUNCTION_BASED_VIEW'),
    path('CLASS_BASED_VIEW/',CLASS_BASED_VIEW.as_view(),name='CLASS_BASED_VIEW'),
    path("FUNCTION_HTML/",FUNCTION_HTML, name="FUNCTION_HTML"),
    path('CLASS_HTML/',CLASS_HTML.as_view(),name='CLASS_HTML'),
    path('FUNCTION_FORM/',FUNCTION_FORM,name='FUNCTION_FORM'),
    path('CLASS_CONTEXT_FORM/',CLASS_CONTEXT_FORM.as_view(),name='CLASS_CONTEXT_FORM'),
    path('HTML_DIRECT/',TemplateView.as_view(template_name='HTML_DIRECT.html'),name='HTML_DIRECT'),
    path('HTML_CONTEXT/',HTML_CONTEXT.as_view(),name='HTML_CONTEXT'),

]
