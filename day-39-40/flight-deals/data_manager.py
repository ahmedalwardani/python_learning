import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b1c1d0ca8e7b71e38309f35a388b1758/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            payload = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}', json=payload)
            print(response.text)