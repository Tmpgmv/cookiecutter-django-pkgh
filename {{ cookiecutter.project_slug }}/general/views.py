from django.http import HttpResponse
from django.views.generic import TemplateView
from general.forms import ModelInputForm


class BaseGeneratorView(TemplateView):
    """
    Базовый генератор кода.
    """
    form_class = ModelInputForm
    repo_task = None
    repo_task_key = None

    # Абстрактные методы для переопределения
    def get_additional_content(self, model_name):
        """Возвращает специфичный для каждого типа генератора контент."""
        raise NotImplementedError

    def get_template_suffix(self):
        """Возвращает суффикс для имени шаблона."""
        raise NotImplementedError

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        if self.repo_task_key and self.repo_task:
            context[self.repo_task_key] = self.repo_task
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model_data = self._process_model_name(form)
            content = self._generate_full_content(model_data)
            return self._create_response(content)
        return super().get(request, *args, **kwargs)

    def _process_model_name(self, form):
        """Обрабатывает имя модели, возвращает словарь с вариантами."""
        model_name_tmp = form.cleaned_data["model_name"].strip()
        return {
            'lower': model_name_tmp.lower(),
            'capitalized': model_name_tmp[0].upper() + model_name_tmp[1:],
            'original': model_name_tmp,
        }

    def _get_model_definition(self, model_name):
        """Генерирует определение модели (общее для всех типов)."""

        html_generator = "html" in self.request.path

        result = f"""
------------------------Модель----------------------------------

from django.db import models
"""
        if html_generator:
            result += """from general.model_mixins import TypicalUrlMixin
"""

        result += f"""
        
        
class {model_name['capitalized']}("""

        if html_generator:
            result += "TypicalUrlMixin, "
        result += """models.Model):



    def __str__(self):
        {% raw %}
        return f"Id: { self.pk }"
        {% endraw %}


    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
        ordering = ["pk"]
"""
        if html_generator:
            result += """            
        # constraints = [
        #     models.CheckConstraint(
        #         condition=Q(time_spent__gt=0),
        #         name="time_spent_gt_0",
        #     )
        # ]"""
        else:
            result += """
            #db_table = "reauests" """
        result += """
        
        
        
        
        """
        

        return result

    def _generate_full_content(self, model_name):
        """Генерирует полный контент, комбинируя общую и специфичную части."""
        model_def = self._get_model_definition(model_name)
        additional = self.get_additional_content(model_name)
        return model_def + additional

    def _create_response(self, content):
        """Создает HTTP ответ с контентом."""
        response = HttpResponse(content.encode('utf-8'))
        response['Content-Type'] = 'text/plain; charset=utf-8'
        return response


class HtmlGeneratorView(BaseGeneratorView):
    """
    Генератор кода для классического веб-приложения.

    См. комментарий в general/view_mixins.py/GetVerboseNameMixin
    """
    template_name = "generators/html_generator.html"
    repo_task = "grablevskiy_mv_computer5_task1"
    repo_task_key = "repo_task_1"

    def get_additional_content(self, model_name):
        """Возвращает специфичный для HTML-генератора контент."""
        model_lower = model_name['lower']
        model_cap = model_name['capitalized']

        return f"""
------------------------Регистрации модели в админке----------------------------------

from django.contrib import admin
from general.admin import BaseAdmin


class {model_cap}Admin(BaseAdmin):
    exclude = []

admin.site.register({model_cap}, {model_cap}Admin)





------------------------Представления----------------------------------

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from general.view_mixins import GetVerboseNameMixin


class {model_cap}ListView(GetVerboseNameMixin,
                    ListView):
    model = {model_cap}

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



class {model_cap}DetailView(GetVerboseNameMixin,
                      DetailView):
    model = {model_cap}
    template_name = "general/pages/detail.html"


class {model_cap}UpdateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      UpdateView):
    model = {model_cap}
    fields = "__all__"    
    #form_class = {model_cap}Form
    success_message = "Сохранено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/form.html"


class {model_cap}CreateView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      CreateView):
    model = {model_cap}
    fields = "__all__"
    #form_class = {model_cap}Form
    success_message = "Сохранено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/form.html"


class {model_cap}DeleteView(SuccessMessageMixin,
                      GetVerboseNameMixin,
                      DeleteView):
    model = {model_cap}
    success_message = "Удалено."
    success_url = reverse_lazy("home")
    template_name = "general/pages/confirm_delete.html"




------------------------URL для CRUD----------------------------------

path("{model_lower}/detail/<int:pk>", {model_cap}DetailView.as_view(), name="{model_lower}_detail"),
path("{model_lower}/update/<int:pk>", {model_cap}UpdateView.as_view(), name="{model_lower}_update"),
path("{model_lower}/delete/<int:pk>", {model_cap}DeleteView.as_view(), name="{model_lower}_delete"),
path("{model_lower}/create", {model_cap}CreateView.as_view(), name="{model_lower}_create"),
path("{model_lower}/list", {model_cap}ListView.as_view(), name="{model_lower}_list"),




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

        return reverse_lazy("{model_lower}_list")





------------------------Форма----------------------------------

from django.forms import ModelForm
from django import forms


class {model_cap}Form(ModelForm):



    class Meta:
        model = {model_cap}
        fields = "__all__"

        {% raw %}
        widgets = {{ # Искать в документации по DateInput.
            'start': forms.DateInput(attrs={{"type": "date"}}, format="%Y-%m-%d"),
        }}
        {% endraw %}
        

"""


class JsonGeneratorView(BaseGeneratorView):
    """
    Генератор кода для REST-приложения.
    """
    template_name = "generators/json_generator.html"
    repo_task = "grablevskiy_mv_computer5_task2"
    repo_task_key = "repo_task_2"

    def get_additional_content(self, model_name):
        """
        Возвращает специфичный для REST-генератора контент.
        В данном случае - пока ничего дополнительного, только модель.
        """
        return ""
