import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if not response.ok:
            print("Failed to retrieve data.")
        else:
            return response.content

    def load_json(self):
        try:
            body = self.get_response_body()
            return json.loads(body)
        except ValueError as e:
            print("Couldn't parse JSON:", e)
            
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)
data = requester.load_json()
print(data)