import json
import requests

api_key = 1085675e0eedfd7ad38b8f58051c33848415cd0e                %using key from govrnment's site
app_token = app140774a8a1b22994f3b74aea8abaf77ef8cfd073           %token for access to info
deputi_name = "Жириновский"                                       %chosen deputi for checking
deputi_api = "http://api.duma.gov.ru/api/{}/deputies.json?app_token={}&begin={}".format(api_key, app_token, deputi_name)

r = requests.get(deputy_api)                                      %request for info from gos.duma's site
json_data = json (r.text)
print (json_data)
deputy_id = json_data[0]["id"]

voted_api = "http://api.duma.gov.ru/api/{}/votesearch.json?app_token"{}&deputy"{}".format(api_key, app_token, deputy_id)
r = requests.get (votes_api)
json_data = json.loads (r.text)
totalCount = int (json_data["totalCount"])
pageSize = int [json_data["pagesize"])
pages = int (total) Count/pagesize
if totalCount & pageSize :=0;
pages +=1

for page in range (1, pages+1, 1);
url = votes_api + "&page={}".format (page)
r = requests.get(votes_api)
json_data = json.loads (r.text)
data = json_data[0]
print(json_data)
