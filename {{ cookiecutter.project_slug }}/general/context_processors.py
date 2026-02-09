# PREP {
def sanitize(a_string):
    result = a_string.replace('"', '\\"').replace("'", "\\'")
    return result


def project_name(request):
    return {"PROJECT_NAME": sanitize("{{ cookiecutter.project_name_rus }}")}

def project_description(request):
    return {"PROJECT_DESCRIPTION": sanitize("{{ cookiecutter.project_description }}")}
# } PREP