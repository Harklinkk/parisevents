import requests

class Client:
    def __init__(self, tags):
        self.tags = tags

    def get_tags(self):
        return self.tags

class APIResponse:
    def __init__(self, tags):
        self.tags=tags

    def JsonResponse(self):
        client = Client(self.tags)
        tags = ""
        for tag in client.get_tags():
            tags += tag
        x = requests.get("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/que-faire-a-paris-/records", {"tags":tags,"limit":"5"})
        json_response = x.json()
        return json_response
        
    def JsonParser(json_response):
        return json_response.loads()

class ClientAgenda:
    def CreateCalendar():
        pass

    def AddEventtoCalendar():
        pass




