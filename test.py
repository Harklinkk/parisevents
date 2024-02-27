from parisplanner import Client,APIResponse

def test_get_client_tags():
    client = Client(["aventure","musique","lol"])
    expected = ["aventure","musique","lol"]
    assert expected == client.get_tags()

def test_get_events_depending_on_client_tags():
    client = Client(["Peinture","Art contemporain"])
    apiresponse = APIResponse(client.get_tags())
    #print (apiresponse.JsonResponse())
    print(apiresponse.JsonResponse())

test_get_events_depending_on_client_tags()