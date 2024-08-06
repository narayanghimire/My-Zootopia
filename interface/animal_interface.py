from abc import ABC, abstractmethod
from model.animal import AnimalModel


class AnimalInterface(ABC):
    @abstractmethod
    def extract_animal_info(self) -> AnimalModel:
        pass

    @abstractmethod
    def display_animal_info(self, animal: AnimalModel):
        pass
