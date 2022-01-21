from collections import OrderedDict

import requests

from functools import lru_cache


@lru_cache(maxsize=None)
def _get_hostname():
    try:
        response = requests.get('http://169.254.169.254/latest/meta-data/hostname')
        return response.text
    except requests.exceptions.ConnectionError:
        return 'not aws environment'


class EC2Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response, 'data'):
            response.data['ec2_instance'] = _get_hostname()
            response.data.move_to_end('ec2_instance', last=False)
        return response
