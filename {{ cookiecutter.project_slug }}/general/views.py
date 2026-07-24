from django.http import HttpResponse
from django.views.generic import TemplateView

from general.forms import ModelInputForm


class UrlPatternView(TemplateView):
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
"""

            return HttpResponse(text_content, content_type="text/plain")

    def get_context_data(self, **kwargs):
        context = super(UrlPatternView, self).get_context_data(**kwargs)
        form = ModelInputForm()
        context['form'] = form
        return context
