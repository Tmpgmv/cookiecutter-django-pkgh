STUDENT_FULL_NAME_RUS = "{{ cookiecutter.student_full_name_rus|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
STUDENT_FULL_NAME_LAT = "{{ cookiecutter.student_full_name_lat|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
PROJECT_NAME_RUS = "{{ cookiecutter.project_name_rus|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
PROJECT_NAME_LAT = "{{ cookiecutter.project_name_lat|replace('\"', '\\\"')||replace('\'', '\\\'')|trim() }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug|replace(' ', '_')|replace('-', '_')|replace(',', '')|replace('.', '')|replace('\"', '')|replace('\'', "")|trim() }}"
PROJECT_DESCRIPTION =  "{{ cookiecutter.project_description|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
MAIN_BACKGROUND_COLOR = "{{ cookiecutter.main_background_color|trim() }}"
AUX_BACKGROUND_COLOR = "{{ cookiecutter.aux_background_color|trim() }}"
ATTENTION_COLOR = "{{ cookiecutter.attention_color|trim() }}"
CUSTOM_USER = {% if cookiecutter.custom_user|trim() == "y" %}True{% else %}False{% endif %}
LOGIN_REQUIRED = {% if cookiecutter.login_required|trim() == "y" %}True{% else %}False{% endif %}
STUDENT_SLUG = "{{ cookiecutter.student_slug }}"