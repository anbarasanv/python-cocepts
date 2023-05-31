import requests
import json
from typing import List
class Fetch:
    def __init__(self, url:str) -> None:
        self.url = url
    def __enter__(self) -> object:
        try:
            self.__response = requests.get(self.url)
            self.json_data = json.loads(self.__response.text)
            return self.json_data
        except requests.exceptions.HTTPError as e:
            print(e)
    def __exit__(self, exc_type, exc_value, exc_traceback):
        del self.json_data

with Fetch("https://jsonplaceholder.typicode.com/users") as fetch:
    print(fetch)
