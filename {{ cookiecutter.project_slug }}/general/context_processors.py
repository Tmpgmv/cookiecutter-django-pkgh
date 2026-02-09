# PREP {
def project_name(request):
    return {"PROJECT_NAME": str({{ cookiecutter.project_name_rus }})}

def project_description(request):
    return {"PROJECT_DESCRIPTION": str({{ cookiecutter.project_description }})}
# } PREP