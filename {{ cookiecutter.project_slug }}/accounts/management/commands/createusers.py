from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import OperationalError

User = get_user_model()  # UNIVERSAL: works with any AUTH_USER_MODEL


class Command(BaseCommand):
    help = 'Create users.'

    USER_GROUP = {
        "a": "Администратор",
        "c": "Авторизированный клиент",
        "m": "Менеджер",
        "g": "Гость",
    }

    def create_auth_groups(self):
        groups = {}

        for code, group_name in self.USER_GROUP.items():
            group, created = Group.objects.get_or_create(name=group_name)
            groups[code] = group

        return groups


    def create_users(self):
        USERS = ["a", "c", "m", "g"]

        for username in USERS:
            if username == "a":
                User.objects.create_superuser(
                    username='a', email='a@a.ru', password='a'
                )
            else:
                User.objects.create_user(
                        username=username, email=f'{username}@{username}.ru', password=username
                    )


    def assign_groups_to_users(self):
        groups = self.create_auth_groups()

        for username, group in groups.items():
            user = User.objects.get(username=username)
            user.groups.add(group)


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Users are being created!'))

        try:
            self.create_auth_groups()
            self.create_users()
            self.assign_groups_to_users()
        except OperationalError as e:
            self.stdout.write(self.style.ERROR("❌ " + e))
            self.stdout.write(self.style.ERROR("========="))
            self.stdout.write(self.style.ERROR("Попробуйте"))
            self.stdout.write(self.style.ERROR("python manage.py makemigrations"))
            self.stdout.write(self.style.ERROR("python manage.py migrate"))


        self.stdout.write(self.style.SUCCESS('Success!'))
