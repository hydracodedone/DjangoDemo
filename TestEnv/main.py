import os

import django

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FirstProject.settings")
    django.setup()
