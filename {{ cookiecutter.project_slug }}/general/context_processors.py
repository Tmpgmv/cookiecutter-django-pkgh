def project_context(request):
    return {
        "PROJECT_NAME": "{{ cookiecutter.project_name_rus }}",
        "PROJECT_DESCRIPTION": "{{ cookiecutter.project_description }}",
    }