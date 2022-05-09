"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf.urls.static import*
from django.conf import settings

from . views import accueil_view, actualites_view, actualite_detail_view, inscription_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Les routes côté utilisateur
    path('', accueil_view, name = "accueil_url"),
    path('actualites/', actualites_view, name = "actualites_url"),
    path('actualite-detail/<int:id>/', actualite_detail_view, name = "actualite_detail_url"),
    path('inscription/', inscription_view, name = "inscription_url"),
    path('contacts/', contact_view, name = "contact_url"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)