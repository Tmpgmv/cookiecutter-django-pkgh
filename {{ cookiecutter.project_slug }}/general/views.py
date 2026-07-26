from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from general.forms import ModelInputForm
from django.utils.decorators import method_decorator

class GeneratorView(TemplateView):
    """
    Генератор кода.
       
    См. комментарий в general/view_mixins.py/GetVerboseNameMixin

    """
    
    template_name = "general/generator.html"

    def post(self, request, *args, **kwargs):
        form = ModelInputForm(request.POST)
        if form.is_valid():
            model_name_lower = form.cleaned_data["model_name"].lower().strip()

             # Берем именно то, что пользователь ввел в поле ввода. Не можем просто взять model_name_lower: не получится PascalCase для наименований из нескольких слов.
            model_name_tmp = form.cleaned_data["model_name"].strip()
            model_name_capitalized = model_name_tmp[0].upper() + model_name_tmp[1:]

            text_content = f"""
------------------------Модель----------------------------------

from django.db import models
from general.model_mixins import TypicalUrlMixin


class {model_name_capitalized}(TypicalUrlMixin,
            models.Model):



    def __str__(self):
        {% raw %}
        return f"Id: {{self.pk}}"
        {% endraw %}

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
        ordering = ["pk"]        




            
------------------------Регистрации модели в админке----------------------------------

from django.contrib import admin
from general.admin import BaseAdmin


class {model_name_capitalized}Admin(BaseAdmin):
    exclude = []

admin.site.register({model_name_capitalized}, {model_name_capitalized}Admin)





------------------------Представления----------------------------------

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from general.view_mixins import GetVerboseNameMixin


class {model_name_capitalized}ListView(GetVerboseNameMixin,
                    ListView):
    model = {model_name_capitalized}

    # Если требуется фильтрация, сортировка и поиск.

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # Получаем параметры из GET-запроса
    #     search = self.request.GET.get('search')
    #     sort = self.request.GET.get('sort')
    #     filter = self.request.GET.get('filter')
    #
    #     if search:
    #         queryset = queryset.filter(number=search)
    #     if filter:
    #         queryset = queryset.filter(status=filter)
    #     if sort:
    #         queryset = queryset.order_by(sort)
    #     # Если sort не передан, используем сортировку по умолчанию из модели (Meta)
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Передаём GET-данные в форму, чтобы она отображала текущие значения
    #     context['form'] = SearchSortFilterForm(self.request.GET or None)
    #     return context



class {model_name_capitalized}DetailView(GetVerboseNameMixin,
                      DetailView):
    model = {model_name_capitalized}
    template_name = "general/pages/detail.html"


class {model_name_capitalized}UpdateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      UpdateView):
    model = {model_name_capitalized}
    fields = "__all__"    
    #form_class = {model_name_capitalized}Form
    success_message = "Сохранено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/form.html"


class {model_name_capitalized}CreateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      CreateView):
    model = {model_name_capitalized}
    fields = "__all__"
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




------------------------URL для CRUD----------------------------------
            
path("{model_name_lower}/detail/<int:pk>", {model_name_capitalized}DetailView.as_view(), name="{model_name_lower}_detail"),
path("{model_name_lower}/update/<int:pk>", {model_name_capitalized}UpdateView.as_view(), name="{model_name_lower}_update"),
path("{model_name_lower}/delete/<int:pk>", {model_name_capitalized}DeleteView.as_view(), name="{model_name_lower}_delete"),
path("{model_name_lower}/create", {model_name_capitalized}CreateView.as_view(), name="{model_name_lower}_create"),
path("{model_name_lower}/list", {model_name_capitalized}ListView.as_view(), name="{model_name_lower}_list"),




------------------------Форма фильтрации, сортировки и поиска ----------------------------------

class SearchSortFilterForm(forms.Form):

    search = forms.IntegerField(required=False,
                                validators=[MinValueValidator(0),],    
                                label="Номер")


    # Как вариант - первым элементом кортежа задавать
    # наименование поля в модели (по которому собрались сортировать). Допустим, модель такая.
    # class Plane(TypicalUrlMixin,
    #            models.Model):
    #    start = models.DateField(verbose_name="Дата ввода в эксплуатацию")
    # Как применять - см. комментарий к HomeView.

    SORT_CHOICES = [
        ('-start', 'Сначала новые ▲'),
        ('start', 'Сначала старые ▼'),
    ]
    sort = forms.ChoiceField(
           choices=SORT_CHOICES,
           initial='-start', # Не должно расходиться с сортировкой по умолчанию в модели (в Meta). 
           required=True,
           label="Дата ввода в эксплуатацию"
    )

    # filter = forms.ModelChoiceField(queryset=Category.objects.all(),
    #                                 empty_label="-- Все категории --", # Изменить по необходимости.
    #                                 required=True
    # )

    filter = forms.ChoiceField(choices=choices(["Все статусы"] + STATUSES),
                               required=False,
                               label="Статус")





------------------------Представление для хомяка----------------------------------

from django.urls import reverse_lazy
from django.views.generic import RedirectView


class HomeView(RedirectView):
    permanent = True
    query_string = True


    def get_redirect_url(self, *args, **kwargs):

        return reverse_lazy("{model_name_lower}_list")





------------------------Форма----------------------------------

from django.forms import ModelForm
from django import forms


class {model_name_capitalized}Form(ModelForm):



    class Meta:
        model = {model_name_capitalized}
        fields = "__all__"
        {% raw %}
        widgets = {{ # Искать в документации по DateInput.
            'start': forms.DateInput(attrs={{"type": "date"}}, format="%Y-%m-%d"),
        }}
        {% endraw %}
"""

            response = HttpResponse(text_content.encode('utf-8'))
            response['Content-Type'] = 'text/plain; charset=utf-8'

            return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ModelInputForm()
        context['form'] = form
        context['repo_task_1'] = "{{ cookiecutter.student_slug }}_computer{{ cookiecutter.computer_number }}_task1"
        context['repo_task_2'] = "{{ cookiecutter.student_slug }}_computer{{ cookiecutter.computer_number }}_task2"
        return context





