from interface.animal_client_interface import AnimalClientInterface
from interface.animal_interface import AnimalInterface
from model.animal import AnimalModel


class AnimalService(AnimalInterface):
    def __init__(self, animal_client: AnimalClientInterface):
        """Initialize with an AnimalClientInterface instance."""
        self.animal_client = animal_client

    def fetch_animal_data(self, animal_name: str) -> str:
        """Fetch animal data from the API."""
        if not animal_name:
            raise ValueError("Animal name is required")

        return  self.animal_client.fetch_animal_data(animal_name)

    def extract_animal_info(self, animal_data: dict) -> AnimalModel:
        """Extracts animal data from json and returns an AnimalModel"""
        name = animal_data.get("name")
        characteristics = animal_data.get("characteristics", {})
        diet = characteristics.get("diet")
        locations = animal_data.get("locations", [])
        location = locations[0] if locations else None
        type_ = characteristics.get("type")

        return AnimalModel(name, diet, location, type_)

