# Санкт-Петербургское государственное бюджетное профессиональное образовательное учреждение "Политехнический колледж городского хозяйства"

## 09.02.07 Информационные системы и программирование (Программист)

---

## Экзаменационная работа `{{ cookiecutter.project_name_rus }}`
Выполнил: {{ cookiecutter.student_full_name_rus }}

{{ cookiecutter.project_description }}


## Создание виртуального окружения
```bash 
python -m venv .venv
```

## Активация виртуального окружения
```bash 
.venv\Scripts\activate  # Windows

source .venv/bin/activate # Linux/MacOS
```

## Установка
```bash 
python -m pip install -r requirements.txt
```

## Применение миграций
```bash
python manage.py migrate
```

## Создать пользователя
```bash
python manage.py createsuperuser
```

## Запуск сервера
```bash
python manage.py runserver
```

## Сброс миграций
```commandline
# 1. Останови Django сервер (Ctrl+C)

# 2. Удали все миграции
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# 3. Удали БД: 
Если используется PostgreSQL
dropdb your_db_name
createdb your_db_name


Если используется SQLite
rm db.sqlite3


# 4. Создай новые миграции
python manage.py makemigrations

# 5. Примени их
python manage.py migrate

```
