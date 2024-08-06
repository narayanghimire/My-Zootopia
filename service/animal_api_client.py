import os

import requests
from interface.animal_client_interface import AnimalClientInterface
from dotenv import load_dotenv

load_dotenv()
class AnimalApiClient(AnimalClientInterface):
    API_URL = "https://api.api-ninjas.com/v1/animals"

    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv('API_KEY')
        if not self.API_KEY:
            raise Exception("Animal API Key not found in environment variables.")

    def fetch_animal_data(self, animal_name: str) -> str:
        """Fetch animal data from the API based on the animal name."""
        url = f"{self.API_URL}?name={animal_name}"
        headers = {
            'X-Api-Key': self.API_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch animal data.")
