from django.contrib import admin

# PREP {
from accounts.models import User

admin.site.register(User)

# } PREP