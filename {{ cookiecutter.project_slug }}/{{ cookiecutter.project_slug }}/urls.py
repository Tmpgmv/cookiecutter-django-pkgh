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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
{% if cookiecutter.login_required %}
from django.contrib.auth.decorators import login_required
{% endif %}
from django.urls import path, include
from django.conf import settings  # PREP
from django.conf.urls.static import static  # PREP
from general.views import UrlPatternView
from home.views import HomeView

"""
    См. комментарий в general/view_mixins.py.
    Чтобы все заработало, нужно URL для CRUD делать по образцу (в части path и name).
    Здесь модель называется Plane:

    urlpatterns = [
        path("plane/detail/<int:pk>", PlaneDetailView.as_view(), name="plane_detail"),
        path("plane/update/<int:pk>", PlaneUpdateView.as_view(), name="plane_update"),
        path("plane/delete/<int:pk>", PlaneDeleteView.as_view(), name="plane_delete"),
        path("plane/create", PlaneCreateView.as_view(), name="plane_create"),
    ]

    Используйте вспомогательную утилиту http://127.0.0.1:8000/aux-url


"""


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    {% if cookiecutter.login_required | trim | lower in ['y', 'yes', 'true', '1'] or cookiecutter.login_required == True %}
    path("", login_required(HomeView.as_view()), name="home"),
    {% else %}
    path("", HomeView.as_view(), name="home"),
    {% endif %}    
    path("admin/", admin.site.urls),
    path("admin-react/", include("django_admin_react.urls")),
    path("admin-api/", include("django_admin_rest_api.urls")),
    path("aux-url/", UrlPatternView.as_view(), name="aux_url"),
]

urlpatterns += i18n_patterns(

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
