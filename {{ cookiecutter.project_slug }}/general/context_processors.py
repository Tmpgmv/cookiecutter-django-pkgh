# PREP {
def sanitize(a_string):
    """
    Превратить строку в литерал Python.
    Иначе: надо санировать данные от пользователя.
    Иначе получим что-то вроде этого:
        return {"PROJECT_NAME": "ООО "Обувь""}
                                ^^^^^^^^^^^
        SyntaxError: invalid syntax. Perhaps you forgot a comma?

    Наша задача вернуть "ООО \"Обувь\"" в данном случае.
    """
    result = a_string.replace('"', '\\"').replace("'", "\\'")
    return result


def project_name(request):
    return {"PROJECT_NAME": sanitize("{{ cookiecutter.project_name_rus }}")}

def project_description(request):
    return {"PROJECT_DESCRIPTION": sanitize("{{ cookiecutter.project_description }}")}
# } PREP