from django.conf import settings

def project_context(request):
    return {
        "PROJECT_NAME": settings.project_name_rus,
        "PROJECT_DESCRIPTION": settings.project_description,
    }