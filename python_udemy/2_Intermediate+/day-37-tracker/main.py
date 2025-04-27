import requests

USER = "sabinasz1"
TOKEN =  "...."
pixela_endpoint = 'https://pixe.la/v1/users'
GRAPHID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}
#########################################
# user_params = {"token": TOKEN,
#                "username": USER,
#                "agreeTermsOfService": "yes",
#                "notMinor": "yes"}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
#########################################

# graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
#
# graph_config = {
#     "id": GRAPHID,
#     "name": "Cycling graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
#     }
#
#
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

#########################################

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}"
graph_endpoint_put = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}/20241211"

graph_input = {
    "date": "20241211",
    "quantity": "20",
    }
graph_input_put = {
    "quantity": "0",
    }

response = requests.post(url=graph_endpoint,json=graph_input, headers=headers)
# response = requests.put(url=graph_endpoint_put,json=graph_input_put, headers=headers)
print(response.text)

#### LINK  - https://pixe.la/v1/users/sabinasz1/graphs/graph1.html