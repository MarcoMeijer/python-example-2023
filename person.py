import requests
import json


class Person:

    def __init__(self, name, age=None):
        self.name = name
        if age == None:
            fetch_result = self.fetch_age()
            if fetch_result == "bad response":
                self.age = None
            else:
                self.age = fetch_result
        else:
            self.age = age

    def fetch_age(self):
        result = requests.get(f'https://api.agify.io/?name={self.name}')
        if result.ok:
            result_json = json.loads(result.text)
            return result_json["age"]
        else:
            return "bad response"

