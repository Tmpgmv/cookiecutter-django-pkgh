from concurrency.exceptions import RecordModifiedError, VersionChangedError, VersionError


class ConcurrentUpdateMixin:
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except (RecordModifiedError, VersionChangedError, VersionError):

            form.add_error(None,
                           "⚠️ Объект изменён другим пользователем! "
                           "Вернитесь в список и откройте заново."
                           )
            return self.form_invalid(form)



class GetVerboseNameMixin:
    """
    В шаблонах general (в частности, detail.html, primitive_list.html)
    выводятся данные об объектах.

    Для заголовка и т.п. хочется знать,
    как же называется модель, которую мы отображаем.

    Которая model:

    class ArticleDetailView(DetailView):
        model = Article

    class ArticleListView(ListView):
        model = Article


    Для этого модель должна иметь соответствующие данные в классе Meta:

    class Plane(models.Model):

        ...

        class Meta:
            verbose_name = "Cамолет"
            verbose_name_plural = "Cамолеты"

    Важно: 
    Работает связка: 
    1. GetVerboseNameMixin (обязательно наследовать от 
    этого класса наряду ListView, CreateView, UpdateView, DeleteView).
    2. urlpatterns. Обязательно называть по образцу (здесь модель называется Plane):

    urlpatterns = [
    path("plane/detail/<int:pk>", PlaneDetailView.as_view(), name="plane_detail"),
    path("plane/update/<int:pk>", PlaneUpdateView.as_view(), name="plane_update"),
    path("plane/delete/<int:pk>", PlaneDeleteView.as_view(), name="plane_delete"),
    path("plane/create", PlaneCreateView.as_view(), name="plane_create"),

]
            
    """


    def get_verbose_name_plural(self):
        return self.model._meta.verbose_name_plural

    def get_verbose_name(self):
        return self.model._meta.verbose_name

    def get_model_name(self):
        return self.model._meta.model_name
