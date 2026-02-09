# # PREP {
# def sanitize(a_string):
#     """
#     Превратить строку в литерал Python.
#     Иначе: надо санировать данные от пользователя.
#     Иначе получим что-то вроде этого:
#         return {"PROJECT_NAME": "ООО "Обувь""}
#                                 ^^^^^^^^^^^
#         SyntaxError: invalid syntax. Perhaps you forgot a comma?
#
#     Наша задача вернуть "ООО \"Обувь\"" в данном случае.
#     """
#     result = a_string.replace('"', '\\"').replace("'", "\\'")
#     return result
#
#
# def project_name(request):
#     return {"PROJECT_NAME": "{{ cookiecutter._project_name_rus }}"}
#
# def project_description(request):
#     return {"PROJECT_DESCRIPTION": "{{ cookiecutter._project_description }}"}
# # } PREP


# def sanitize_string(value):
#     """Escape quotes for Python string literals."""
#     return (value.replace('\\', '\\\\')
#                  .replace('"', '\\"')
#                  .replace("'", "\\'"))

def project_context(request):
    return {
        "PROJECT_NAME": "PLACEHOLDER_NAME",
        "PROJECT_DESCRIPTION": "PLACEHOLDER_DESCRIPTION",
    }