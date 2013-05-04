# Django settings for shopping project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath('./')

# To Chnage Admins Add here to overwrite the main settings file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_shop', 
        'USER': 'chris_dev', 
        'PASSWORD': 'dev', 
        'HOST': '', 
        'PORT': '', 
    }
}

MEDIA_ROOT = os.path.join('media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)