from django.db import models

{% if cookiecutter.custom_user | trim | lower in ['y', 'yes', 'true', '1'] or cookiecutter.custom_user == True %}
# PREP {
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Расширенная модель пользователя системы.
    Добавлено отчество и методы, в частности, для работы с ролями.
    """
    
    patronymic = models.CharField(max_length=300,
                                  verbose_name="Отчество")

    def get_full_name(self):
        return super().first_name + " " + self.patronymic + " " + super().last_name

    def is_admin(self):
        result = self.groups.filter(name='Администратор').exists() or self.is_superuser
        return result

    def is_manager(self):
        return self.groups.filter(name='Менеджер').exists()

    def is_client(self):
        return self.groups.filter(name__icontains='авторизированный').exists()        

    def __str__(self):
        return self.get_full_name()

    def role(self):
        return self.groups.first() or ""

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

# } PREP

{% endif %}
