from abc import ABC, abstractmethod
from model.animal import AnimalModel


class AnimalHTMLInterface(ABC):

    @abstractmethod
    def format_animal_info(self, animal: AnimalModel) -> str:
        pass

    @abstractmethod
    def read_animal_template(self, template_path) -> str:
        pass