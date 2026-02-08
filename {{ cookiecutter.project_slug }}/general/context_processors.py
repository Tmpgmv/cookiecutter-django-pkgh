from django.conf import settings # PREP

def app_name(request): # PREP
    return {'APP_NAME': settings.APP_NAME} # PREP