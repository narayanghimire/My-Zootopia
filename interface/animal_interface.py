from abc import ABC, abstractmethod
from model.animal import AnimalModel


class AnimalInterface(ABC):
    @abstractmethod
    def extract_animal_info(self, animal_data: dict) -> AnimalModel:
        pass

    @abstractmethod
    def fetch_animal_data(self, animal_name: str) -> str:
        pass
