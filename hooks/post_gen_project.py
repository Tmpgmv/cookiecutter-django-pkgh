#!/usr/bin/env python
"""Post-generation hook to sanitize user input into context processors."""
import os
import re

def sanitize(value):
    return (value.replace('\\', '\\\\')
                 .replace('"', '\\"')
                 .replace("'", "\\'"))

# Read Cookiecutter context (exists only during generation)
cookiecutter_dict = {{cookiecutter}}

# Sanitized values
safe_name = sanitize(cookiecutter_dict['project_name_rus'])
safe_desc = sanitize(cookiecutter_dict['project_description'])

# Inject into context_processors.py
cp_file = os.path.join('general', 'context_processors.py')
with open(cp_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'PROJECT_NAME\s*=\s*"[^"]*"', f'PROJECT_NAME = "{safe_name}"', content)
content = re.sub(r'PROJECT_DESCRIPTION\s*=\s*"[^"]*"', f'PROJECT_DESCRIPTION = "{safe_desc}"', content)

with open(cp_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Context processors updated with sanitized values")
