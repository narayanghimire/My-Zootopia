from abc import ABC, abstractmethod


class AnimalClientInterface(ABC):

    @abstractmethod
    def fetch_animal_data(self, animal_name: str) -> str:
        """Fetch animal data from the API based on the animal name."""
        pass