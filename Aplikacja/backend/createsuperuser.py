from django.db import IntegrityError
from django.contrib.auth.models import User

import environ # This package import from 'django-environ' https://pypi.org/project/django-environ/
env = environ.Env(
    DEBUG=(bool, False)
)

try:
    superuser = User.objects.create_superuser(
        username=env('SUPER_USER_NAME', default="admin"),
        email=env('SUPER_USER_EMAIL', default="admin@gmail.com"),
        password=env('SUPER_USER_PASSWORD', default="1234"))
    superuser.save()
except IntegrityError:
    print(f"Super User with username {env('SUPER_USER_NAME')} is already exit!")
except Exception as e:
    print(e)
