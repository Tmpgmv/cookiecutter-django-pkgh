from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

{% if cookiecutter.custom_user == "y" %}

# PREP {
from .models import User

admin.site.register(User, UserAdmin)

# } PREP

{% endif %}