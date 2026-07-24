{% comment %}
  Применяется совместно с 

search-sort-filter.js

{% endcomment %}


class SearchSortFilterForm(forms.Form):
    CHOICES = [
        ('more', 'Больше'),
        ('less', 'Меньше'),
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
