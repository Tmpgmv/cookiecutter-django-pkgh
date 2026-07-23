import os
import sys
import threading
import time
import webview
from django.core.management import execute_from_command_line


def start_django():
    """Starts the Django development server in a background thread."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'marverl_boots.settings')  # <-- CHANGE 'myproject' to your actual project name

    # Force Django to run without the auto-reloader to avoid breaking threads
    sys.argv = ['manage.py', 'runserver', '127.0.0.1:8000', '--noreload']
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # 1. Start Django backend in the background
    django_thread = threading.Thread(target=start_django, daemon=True)
    django_thread.start()

    # 2. Wait a brief moment for the Django server to spin up
    time.sleep(1)

    # 3. Open the native desktop window pointing to the local app
    webview.create_window(
        title="Чудо-обувь",
        url="http://127.0.0.1:8000",
        width=1024,
        height=768,
        resizable=True
    )

    # 4. Start the GUI loop (closing this window kills the background Django server)
    webview.start()
