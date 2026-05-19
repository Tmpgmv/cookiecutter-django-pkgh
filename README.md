# Шаблон проекта для экзаменационной работы

## Версия шаблона
1.0

<!---## Установка uv

Windows:
```bash
winget install --id=astral-sh.uv -e
```

```bash
pip install uv
```

-->
## Разворачивание проекта из шаблона

**Установите Cookiecutter в свой venv:**


В колледже:
```bash
pip install --no-index --find-links=D:\dependencies -r D:\dependencies\requirements.txt
```


**Разверните проект из шаблона:**

В колледже:
```bash
$env:PYTHONIOENCODING="utf-8"; $env:LANG="ru_RU.UTF-8"; python -m cookiecutter 'http://gogs.wsr.ru:3000/grab/cookiecutter-django-pkgh.git' custom_user=y login_required=y tests_required=n
```

```bash
python -m cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh --config-file D:\dependencies\config.yaml --no-input
```

Вне колледжа. Windows:
```bash
$env:PYTHONIOENCODING="utf-8"; $env:LANG="ru_RU.UTF-8"; python -m cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh custom_user=y login_required=y tests_required=n
```

Вне колледжа. Linux:
```bash
PYTHONIOENCODING=utf-8 LANG=C.UTF-8 python -m cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh custom_user=y login_required=y tests_required=n
```

```bash
python -m cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh --config-file config.yaml --no-input
```

Вне колледжа:
```bash
pip install -r requirements.txt
```

<!--
В колледже:
```bash
$env:PYTHONIOENCODING="utf-8"; $env:LANG="ru_RU.UTF-8"; uv tool run cookiecutter 'http://gogs.wsr.ru:3000/grab/cookiecutter-django-pkgh.git' custom_user=y login_required=y tests_required=n
```

```bash
python -m cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh --config-file config.yaml --no-input
```

Вне колледжа. Windows:
```bash
$env:PYTHONIOENCODING="utf-8"; $env:LANG="ru_RU.UTF-8"; uv tool run cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh custom_user=y login_required=y tests_required=n
```

Вне колледжа. Linux:
```bash
PYTHONIOENCODING=utf-8 LANG=C.UTF-8 uv tool run cookiecutter gh:Tmpgmv/cookiecutter-django-pkgh custom_user=y login_required=y tests_required=n
```
-->

NB! Когда вы копируете текст из браузера (особенно из GitHub), пробел между словами может 
быть не обычным пробелом (ASCII код 32), а специальным символом Юникода U+00A0 
(non-breaking space).

Однако uv или сам python при чтении аргументов командной строки натыкается на байт 0xC2 0xA0 
(так выглядит неразрывный пробел в UTF-8).

Если библиотека обработки аргументов (в данном случае cookiecutter) ожидает только 
стандартные ASCII-разделители, происходит сбой декодирования.

Иначе говоря, типичная ошибка: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1... 
как раз говорит о том, что парсер "споткнулся" на байте, который он не ожидал увидеть в этой позиции.

Вывод: 

"Очистка" черрез адресную строку: вставьте скопированную команду в адресную строку браузера Chrome, 
а затем скопируйте её оттуда. Браузер нормализуют такие символы.

Теперь вставляйте в терминал.


## Комментарий

При работе Cookiecutter синтаксис Jinja 
кофликтует с синтаксисом Django Template Language.
Поэтому все html-файлы исключены из поля зрения Cookiecutter.

Однако, переменные переданы в контекст 
через context processors, что позволило 
отобразить данные в шаблонах.

## cookiecutter.json

**`student_full_name_rus`** - ФИО студента. Необходимо для документации проекта (README.md).

**`surname_initials_lat`** - ФИО студента латиницей. Нужен только для формирования student_slug.

**`db_username`** - Пользователь БД. См. secret.py.

**`db_password`** - Пароль пользователя БД. См. secret.py.

**`project_name_rus`** - Наименование проекта на русском языке. Может применяться в шаблонах (см. context_processors.py). Также попадает в документацию проекта (README.md).

**`project_name_lat`** - Наименование проекта на латинице. Применяется только в cookiecutter.json для формирования project_slug.

**`project_slug`** - Слаг проекта. Применяется в структуре каталогов проката. А также как часть имени БД.  См. secret.py.

**`project_description`** - Описание проекта. Может применяться в шаблонах (см. context_processors.py). Также попадает в документацию проекта (README.md).

**`main_background_color`** - Цвет. Скорее всего, будет обозначен в приложении к заданию.

**`aux_background_color`** - Цвет. Скорее всего, будет обозначен в приложении к заданию.

**`attention_color`** - Цвет. Скорее всего, будет обозначен в приложении к заданию.

**`custom_user`** - Нужно ли расширять модель пользователя.

**`login_required`** - Нужно ли выполнять вход (не каждый год задание требует авторизации).

**`student_slug`** - Слаг студента. Применяется как часть имени БД.  См. secret.py.

**`tests_required`** - Требуются ли тесты. Не каждый год они нужны. Если тесты сгенерирвать, они станут частью проекта. И за их работоспособность придется отвечать.

## Сброс миграций
### 1. Остановите Django сервер (Ctrl+C)

### 2. Удалите все миграции
**Под Windows:** запустить delete_migrations.bat.

**Под Linux:**
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```

### 3. Удалите БД: 
Если используется PostgreSQL

```bash
dropdb your_db_name
createdb your_db_name
```

Если используется SQLite
```bash
rm db.sqlite3
```

### 4. Создайте новые миграции

```bash
python manage.py makemigrations
```
### 5. Примените их

```bash
python manage.py migrate
```


## Сброс последовательностей

```bash
DO $$
DECLARE
    r RECORD;
    max_id BIGINT;
    seq_name TEXT;
BEGIN
    -- Loop through all columns that have an owned sequence (serial / identity / nextval)
    FOR r IN 
        SELECT 
            tc.table_schema,
            tc.table_name,
            tc.column_name,
            pg_get_serial_sequence(quote_ident(tc.table_schema) || '.' || quote_ident(tc.table_name), tc.column_name) AS sequence_name
        FROM information_schema.columns tc
        WHERE tc.table_schema NOT IN ('pg_catalog', 'information_schema') -- Skip system schemas
          AND pg_get_serial_sequence(quote_ident(tc.table_schema) || '.' || quote_ident(tc.table_name), tc.column_name) IS NOT NULL
    LOOP
        -- Get the current MAX value from the table safely
        EXECUTE format('SELECT COALESCE(MAX(%I), 0) FROM %I.%I', 
                       r.column_name, r.table_schema, r.table_name) INTO max_id;

        -- If the table has rows, update the sequence to point to the MAX(id)
        -- The next nextval() call will automatically return MAX(id) + 1
        IF max_id > 0 THEN
            EXECUTE format('SELECT setval(%L, %s, true)', r.sequence_name, max_id);
        ELSE
            -- If the table is completely empty, reset the sequence to start at 1
            EXECUTE format('SELECT setval(%L, 1, false)', r.sequence_name);
        END IF;
    END LOOP;
END $$;
```
