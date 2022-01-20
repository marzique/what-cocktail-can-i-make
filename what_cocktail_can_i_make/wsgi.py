"""
WSGI config for what_cocktail_can_i_make project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "what_cocktail_can_i_make.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
