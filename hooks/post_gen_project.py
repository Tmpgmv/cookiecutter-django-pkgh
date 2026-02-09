#!/usr/bin/env python3
"""Post-generation hook - NO imports needed for cookiecutter context."""
import re
import os

def sanitize(value):
    return (value.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'"))

# Cookiecutter injects {{cookiecutter}} automatically - just use it directly
cookiecutter_dict = {{cookiecutter}}  # ← This works, no OrderedDict needed

safe_name = sanitize(cookiecutter_dict['project_name_rus'])
safe_desc = sanitize(cookiecutter_dict['project_description'])

# Fix context processor
cp_file = 'general/context_processors.py'
with open(cp_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'PROJECT_NAME\s*=\s*"[^"]*"', f'PROJECT_NAME = "{safe_name}"', content)
content = re.sub(r'PROJECT_DESCRIPTION\s*=\s*"[^"]*"', f'PROJECT_DESCRIPTION = "{safe_desc}"', content)

with open(cp_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Injected: '{safe_name}'")
