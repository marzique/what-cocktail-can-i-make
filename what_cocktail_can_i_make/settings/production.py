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
