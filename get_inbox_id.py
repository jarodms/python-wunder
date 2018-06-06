from myconfig import *
import wunderpy2

api = wunderpy2.WunderApi()
client = api.get_client(access_token, client_id) 

lists = client.get_lists()
list = lists[0]

print(list['id'])

