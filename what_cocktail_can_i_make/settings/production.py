import requests

from .development import *


def get_ec2_instance_ip():
    """Try to obtain the IP address of the current EC2 instance in AWS"""
    try:
        ip = requests.get(
          'http://169.254.169.254/latest/meta-data/local-ipv4',
          timeout=0.01
        ).text
    except requests.exceptions.ConnectionError:
        return None
    return ip


AWS_LOCAL_IP = get_ec2_instance_ip() or '*'
ALLOWED_HOSTS = ['cocktails-dev.eu-central-1.elasticbeanstalk.com', AWS_LOCAL_IP]


if 'AWS_ACCESS_KEY_ID' in os.environ:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = None
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
