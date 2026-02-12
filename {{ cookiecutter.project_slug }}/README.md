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

## Выполнение тестов
```bash
python manage.py test
```

