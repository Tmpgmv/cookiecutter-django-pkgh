from django import template
from django.db.models.fields.files import ImageFieldFile

register = template.Library()


@register.filter
def get_fields(model):
    """
    Возвращает все поля в модели кроме сгенерированных автоматически.
    Не возвращает наборы данных для внешних ключей.
    В модели поля могут быть исключены из выборки
    путем задания EXCLUDE_FROM_DETAIL.

    Применяется совместно с шаблоном general/detail.html.


    Применение:

    class Product(models.Model):
        EXCLUDE_FROM_DETAIL = ['price']


    """
    # Проверяем атрибут класса detail_exclude
    EXCLUDE_FIELDS = getattr(model.__class__, 'EXCLUDE_FROM_DETAIL', [])

    fields = []
    for field in model._meta.get_fields():
        # Исключить наборы данных и автогенерированные поля.
        if field.one_to_many or field.many_to_many or field.auto_created:
            continue

        # Учесть исключенные поля.
        if field.name in EXCLUDE_FIELDS:
            continue

        value = getattr(model, field.name)
        fields.append({
            'label': field.verbose_name,
            'name': field.name,
            'value': value,
            'is_image': isinstance(value, ImageFieldFile),
        })
    return fields