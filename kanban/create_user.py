from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kanban.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    user=User.objects.create_user('admin', password='qwer1234')
    user.is_superuser=True
    user.is_staff=True
    user.save()
    print('\nUser admin was created! password: qwer1234\n')
else:
    print('\nAdmin: \nusername: admin\npassword: qwer1234\n')
