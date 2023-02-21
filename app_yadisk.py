import os
import json
import requests


class YaDisk():
    def __init__(self) -> None:
        """Token, url."""
        self.token = 'ваш_апи_яндекс_диска'
        self.url = 'https://cloud-api.yandex.net/v1/disk/'
    
    def get_header(self) -> dict:
        """Headers."""
        return {'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def make_folder(self, folder: str) -> requests.put:
        """Make folder on yandex disk."""
        url = self.url + 'resources'
        headers = self.get_header()
        params = {'path': folder}
        return requests.put(url, headers=headers, params=params)


def main():
    yadisk = YaDisk()
    print(yadisk.make_folder('asd'))


if __name__ == '__main__':
    main()