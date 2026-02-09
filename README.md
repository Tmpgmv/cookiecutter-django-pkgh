# Шаблон проекта для экзаменационной работы

## Установка

Cookiecutter должен быть установлен system wide, 
т.е. не в виртуальном окружении.

```bash
uv tool run cookiecutter run gh:Tmpgmv/cookiecutter-django-pkgh
```

## Комментарий

При работе Cookiecutter синтаксис Jinja 
кофликтует с синтаксисом Django Template Language.
Поэтому все html-файлы исключены из поля зрения Cookiecutter.

Однако, переменные переданы в контекст 
через context processors, что позволило 
отобразить данные в шаблонах.