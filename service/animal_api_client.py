import requests
from interface.animal_client_interface import AnimalClientInterface


class AnimalApiClient(AnimalClientInterface):
    API_KEY = "v/YVo/vVlM0tlv9Gvq8pRA==JpfSpoX6EqKRqFIH"
    API_URL = "https://api.api-ninjas.com/v1/animals"

    def fetch_animal_data(self, animal_name: str) -> str:
        """Fetch animal data from the API based on the animal name."""
        url = f"{self.API_URL}?name={animal_name}"
        headers = {
            'X-Api-Key': self.API_KEY
        }
        try:
            response = requests.get(url, headers=headers)
            return response.json()
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []
