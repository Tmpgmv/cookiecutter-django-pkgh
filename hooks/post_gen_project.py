#!/usr/bin/env python3
import re

def sanitize(value):
    return (value.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'"))

# Cookiecutter automatically provides {{cookiecutter}} - NO OrderedDict needed
cookiecutter_dict = {{cookiecutter}}

safe_name = sanitize(cookiecutter_dict['project_name_rus'])
safe_desc = sanitize(cookiecutter_dict['project_description'])

# Update context processor
with open('general/context_processors.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('PLACEHOLDER_NAME', safe_name)
content = content.replace('PLACEHOLDER_DESCRIPTION', safe_desc)

with open('general/context_processors.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Injected: '{safe_name}'")
