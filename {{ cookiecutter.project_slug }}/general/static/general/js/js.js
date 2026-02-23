$('#id_stock, #id_supplier').on('change', function() {
        $('#search-sort-filter').submit();
    });


$('#id_search').on('focusout', function() {
        $('#search-sort-filter').submit();
});