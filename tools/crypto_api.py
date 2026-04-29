import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["bpi"]["USD"]["rate"]
    else:
        return "Erreur API"