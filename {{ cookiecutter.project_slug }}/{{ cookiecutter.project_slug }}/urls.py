"""
URL configuration for {{ cookiecutter.project_name_lat }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
{% if cookiecutter.login_required == "y" %}
from django.contrib.auth.decorators import login_required
{% endif %}
from django.urls import path, include
from django.conf import settings  # PREP
from django.conf.urls.static import static  # PREP

from home.views import HomeView

urlpatterns = (
    [
        path("accounts/", include("django.contrib.auth.urls")),
        {% if cookiecutter.login_required %}
        path("", login_required(HomeView.as_view()), name="home"),
        {% else %}
        path("", HomeView.as_view(), name="home"),
        {% endif %}
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
