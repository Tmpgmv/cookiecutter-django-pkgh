from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from general.forms import ModelInputForm
from django.utils.decorators import method_decorator

class UrlPatternView(TemplateView):
    """
    Вспомогательное представление.
    Генерирует для конкретной модели: 
        1. URL для CRUD.
        2. Представления.
        3. Регистрации модели в админке.
        4. Представления для хомяка.
        
    См. комментарий в general/view_mixins.py/GetVerboseNameMixin

    """
    
    template_name = "general/url_patterns.html"

    def post(self, request, *args, **kwargs):
        form = ModelInputForm(request.POST)
        if form.is_valid():
            model_name_lower = form.cleaned_data["model_name"].lower().strip()
            model_name_capitalized = model_name_lower.capitalize()
            text_content = f"""path("{model_name_lower}/detail/<int:pk>", {model_name_capitalized}DetailView.as_view(), name="{model_name_lower}_detail"),
path("{model_name_lower}/update/<int:pk>", {model_name_capitalized}UpdateView.as_view(), name="{model_name_lower}_update"),
path("{model_name_lower}/delete/<int:pk>", {model_name_capitalized}DeleteView.as_view(), name="{model_name_lower}_delete"),
path("{model_name_lower}/create", {model_name_capitalized}CreateView.as_view(), name="{model_name_lower}_create"),






from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from general.view_mixins import GetVerboseNameMixin


class {model_name_capitalized}DetailView(GetVerboseNameMixin,
                      DetailView):
    model = {model_name_capitalized}
    template_name = "general/pages/detail.html"


class {model_name_capitalized}UpdateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      UpdateView):
    model = {model_name_capitalized}
    #form_class = {model_name_capitalized}Form
    success_message = "Сохранено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/form.html"


class {model_name_capitalized}CreateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      CreateView):
    model = {model_name_capitalized}
    #form_class = {model_name_capitalized}Form
    success_message = "Сохранено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/form.html"


class {model_name_capitalized}DeleteView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      DeleteView):
    model = {model_name_capitalized}
    success_message = "Удалено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/confirm_delete.html"






from django.contrib import admin
from general.admin import BaseAdmin

class {model_name_capitalized}Admin(BaseAdmin):
    exclude = []

admin.site.register({model_name_capitalized}, {model_name_capitalized}Admin)






class HomeView(GetVerboseNameMixin,
               ListView):

    model = {model_name_capitalized}
    template_name = "general/pages/list.html"
"""

            response = HttpResponse(text_content.encode('utf-8'))
            response['Content-Type'] = 'text/plain; charset=utf-8'

            return response

    def get_context_data(self, **kwargs):
        context = super(UrlPatternView, self).get_context_data(**kwargs)
        form = ModelInputForm()
        context['form'] = form
        return context
