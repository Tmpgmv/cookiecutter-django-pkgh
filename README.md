# Шаблон проекта для экзаменационной работы

## Версия шаблона
1.0

## Установка

Cookiecutter должен быть установлен system wide, 
т.е. не в виртуальном окружении.

```bash
uv tool run cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh custom_user=y login_required=y tests_required=n
```

## Комментарий

При работе Cookiecutter синтаксис Jinja 
кофликтует с синтаксисом Django Template Language.
Поэтому все html-файлы исключены из поля зрения Cookiecutter.

Однако, переменные переданы в контекст 
через context processors, что позволило 
отобразить данные в шаблонах.

## cookiecutter.json

student_full_name_rus - ФИО студента. Необходимо для документации проекта (README.md).
student_full_name_lat - ФИО студента латиницей. Часть имени БД. См. secret.py.
db_username - Пользователь БД. См. secret.py.
db_passwordт - Пароль пользователя БД. См. secret.py.
project_name_rus - Наименование проекта на русском языке. Может применяться в шаблонах (см. context_processors.py). Также попадает в документацию проекта (README.md).
project_name_lat - Наименование проекта на латинице. Применяется только в cookiecutter.json для формирования project_slug.
project_slug - Слаг проекта. Применяется в структуре каталогов проката. А также как часть имени БД.  См. secret.py.
project_description - Описание проекта. Может применяться в шаблонах (см. context_processors.py). Также попадает в документацию проекта (README.md).
main_background_color - Цвет. Скорее всего, будет обозначен в приложении к заданию.
aux_background_color - Цвет. Скорее всего, будет обозначен в приложении к заданию.
attention_color - Цвет. Скорее всего, будет обозначен в приложении к заданию.
custom_user - Нужно ли расширять модель пользователя.
login_required - Нужно ли выполнять вход (не каждый год задание требует авторизации).
student_slug - Слаг студента. Применяется как часть имени БД.  См. secret.py. 

## Сброс миграций
# 1. Остановите Django сервер (Ctrl+C)

# 2. Удалите все миграции
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# 3. Удалите БД: 
Если используется PostgreSQL
dropdb your_db_name
createdb your_db_name


Если используется SQLite
rm db.sqlite3


# 4. Создайте новые миграции
python manage.py makemigrations

# 5. Примените их
python manage.py migrate
