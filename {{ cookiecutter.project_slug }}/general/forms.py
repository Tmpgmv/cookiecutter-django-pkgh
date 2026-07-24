"""
Форма фильтрации, сортировки и поиска.
См. комментарий в templates/general/embedded/search_sort_filter.html

Эта форма требует доработки. Как минимум заменить Supplier на нужную модель,
а также заменить label для сортировки и фильтрации.
"""

from django.forms import forms

class SearchSortFilterForm(forms.Form):
    CHOICES = [
        ('more', '▲'),
        ('less', '▼'),
    ]

    search = forms.CharField(required=False,
                             label="Поиск")

    sort = forms.ChoiceField(
           choices=CHOICES,
           initial='more',
           required=False,
        label="Количество"
    )

    filter = forms.ModelChoiceField(queryset=Supplier.objects.all(),
                                      empty_label="Все поставщики",
                                      required=False,
                                      label="Поставщик")
