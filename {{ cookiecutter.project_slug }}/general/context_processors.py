# PREP {
def project_name(request):
    return {"PROJECT_NAME": {{ cookiecutter.project_name_rus }}}

def project_description(request):
    return {"PROJECT_DESCRIPTION": {{ cookiecutter.project_description }}}
# } PREP