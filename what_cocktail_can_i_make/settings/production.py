from .development import *

ALLOWED_HOSTS = ['cocktails-dev.eu-central-1.elasticbeanstalk.com']

# Used to authenticate with S3
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    STATICFILES_STORAGE = 'what_cocktail_can_i_make.storage_backends.StaticStorage'
    DEFAULT_FILE_STORAGE = 'what_cocktail_can_i_make.storage_backends.MediaStorage'

CDN_ENABLED = False
AWS_S3_SECURE_URLS = False

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'cocktails-bucket')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN', None)
AWS_QUERYSTRING_AUTH = False

STATIC_LOCATION = 'static'
MEDIA_LOCATION = 'media'

if AWS_S3_CUSTOM_DOMAIN:
    STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATIC_LOCATION)
    MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIA_LOCATION)

    AWS_DEFAULT_ACL = None
