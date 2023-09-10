import datetime

import requests

USERNAME = "celiiik"
TOKEN = "cnvldfwkhaoewfdlmvn"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username':USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "ajisai"
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(graph_response.text)

graph_1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# print(graph_1_endpoint)

now = datetime.datetime.now()
pixel_date = now.strftime("%Y%m%d")

pixel_json = {
    "date": pixel_date,
    "quantity": input("How many days have you finished?"),
    # "optionalData": "Python 100 days of code challenge",
}

pixel_response = requests.post(url=graph_1_endpoint, headers=graph_headers, json=pixel_json)
print(pixel_response.text)

specific_pixel_endpoint = f"{graph_1_endpoint}/{pixel_date}"
specific_pixel_json = {
    "quantity": "1",
}

# pixel_update_response = requests.put(headers=graph_headers, url=specific_pixel_endpoint, json=specific_pixel_json)
# print(pixel_update_response.text)
