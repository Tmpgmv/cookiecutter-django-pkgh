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


        try:
            for code, group_name in self.USER_GROUP.items():
                group, created = Group.objects.get_or_create(name=group_name)
                groups[code] = group
        except OperationalError as e:
            self.stdout.write(self.style.SUCCESS(e))
            print("python manage.py makemigrations")
            print("python manage.py migrate")

        return groups


    def create_users(self):
        USERS = ["a", "c", "m", "g"]

        try:
            for username in USERS:
                if username == "a":
                    User.objects.create_superuser(
                        username='a', email='a@a.ru', password='a'
                    )
                else:
                    User.objects.create_user(
                            username=username, email=f'{username}@{username}.ru', password=username
                        )

        except OperationalError as e:
            self.stdout.write(self.style.SUCCESS(e))
            print("python manage.py makemigrations")
            print("python manage.py migrate")
        except Exception as e:
            self.stdout.write(self.style.SUCCESS(e))


    def assign_groups_to_users(self):
        groups = self.create_auth_groups()

        for username, group in groups.items():
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                continue


            user.groups.clear()
            user.groups.add(group)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Users are being created!'))

        try:
            self.create_auth_groups()
            self.create_users()
            self.assign_groups_to_users()
        except Exception as e:
            self.stdout.write(self.style.SUCCESS(e))

        self.stdout.write(self.style.SUCCESS('Success!'))
