from django.contrib import admin, UserAdmin

{% if cookiecutter.custom_user == "y" %}

# PREP {
from accounts.models import User

admin.site.register(User, UserAdmin)

# } PREP

{% endif %}