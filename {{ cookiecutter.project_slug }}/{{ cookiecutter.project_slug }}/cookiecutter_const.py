# PREP {
STUDENT_FULL_NAME_RUS = "{{ cookiecutter.student_full_name_rus|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
PROJECT_NAME_RUS = "{{ cookiecutter.project_name_rus|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
PROJECT_DESCRIPTION =  "{{ cookiecutter.project_description|replace('\"', '\\\"')|replace('\'', '\\\'')|trim() }}"
MAIN_BACKGROUND_COLOR = "{{ cookiecutter.main_background_color|trim() }}"
AUX_BACKGROUND_COLOR = "{{ cookiecutter.aux_background_color|trim() }}"
ATTENTION_COLOR = "{{ cookiecutter.attention_color|trim() }}"
# } PREP