view_key = 'RY+4N/c2kDqAnmf/1PwAGPdMOt3ipgzXyRCxMN9c+qEqbw8VNnAzEOGeHxPLGukOP9neNeBzY0ZWdyvAHzNr1Q=='

import requests
url = "https://api.exchange.coinbase.com/accounts"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)