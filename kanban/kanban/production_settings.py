DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'db',
        'USER': 'postgres',
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_database_django',
            'USER': 'postgres',
            'HOST': 'db',
        },
    }
}
