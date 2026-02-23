// PREP {

// Шаблон

//{% if user.is_admin or user.is_manager %}
//<div class="container my-4">
//  <table>
//    <form id="search-sort-filter" method="get">
//      {% csrf_token %}
//      {{ form.as_table }}
//    </form>
//  </table>
//</div>
//{% endif %}

// forms.py

//class SearchSortFilterForm(forms.Form):
//    CHOICES = [
//        ('more', 'Больше'),
//        ('less', 'Меньше'),
//    ]
//
//    stock = forms.ChoiceField(
//        choices=CHOICES,
//        initial='more',
//        required=False,
//        label="Количество на складе"
//    )
//
//    search = forms.CharField(required=False,
//                             label="Поиск")
//
//    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),
//                                      empty_label="Все поставщики",
//                                      required=False,
//                                      label="Поставщик")

// Представление:

//class ProductListView(ListView):
//    model = Product
//
//    def get_queryset(self):
//        sort_by_stock = self.request.GET.get("stock", "more")
//        search_phrase = self.request.GET.get("search", None)
//        supplier_id = self.request.GET.get("supplier", None)
//
//        queryset = Product.objects.all()
//        if sort_by_stock == "more":
//            queryset = queryset.order_by("-stock")
//        else:
//            queryset = queryset.order_by("stock")
//
//        if supplier_id:
//            queryset = queryset.filter(supplier_id=supplier_id)
//
//        if search_phrase:
//            queryset = queryset.filter(Q(sku__icontains=search_phrase) |
//                                       Q(product_name__icontains=search_phrase) |
//                                       Q(unit_of_measurement__icontains=search_phrase) |
//                                       Q(product_category__icontains=search_phrase) |
//                                       Q(description__icontains=search_phrase))
//
//        return queryset
//
//    def get_context_data(self, **kwargs):
//        context = super().get_context_data(**kwargs)
//
//        form = SearchSortFilterForm(self.request.GET)
//        context['form'] = form
//        return context


// } PREP

$('#id_stock, #id_supplier').on('change', function() {
        $('#search-sort-filter').submit();
    });


$('#id_search').on('focusout', function() {
        $('#search-sort-filter').submit();
});