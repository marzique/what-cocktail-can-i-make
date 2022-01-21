from typing import Dict

import requests

from django.conf import settings


class PixabayImageService:
    ROOT_URL = 'https://pixabay.com/api/'
    ACCESS_KEY = settings.PIXABAY_KEY

    def _get_response(self, keyword: str):
        data = {}
        params = {'key': self.ACCESS_KEY, 'q': keyword}
        response = requests.get(self.ROOT_URL, params=params)
        if response.status_code == 200:
            data = response.json()
        return data

    @staticmethod
    def _parse_image_url(data: Dict) -> str:
        url = ''
        if data and data['totalHits']:
            url = data['hits'][0].get('webformatURL', '')
        return url

    def get_image_url_by_keyword(self, keyword: str) -> str:
        data = self._get_response(keyword)
        url = self._parse_image_url(data)
        return url
