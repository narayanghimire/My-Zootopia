from abc import ABC, abstractmethod
from model.animal import AnimalModel


class AnimalHTMLInterface(ABC):

    @abstractmethod
    def format_animal_info(self, animal: AnimalModel) -> str:
        pass

    @abstractmethod
    def read_animal_template(self, template_path) -> str:
        """Read the animal template and return it as a string."""
        pass

    def generate_html(self, animal_info: str, animal_name: str):
        """Generates the final HTML content with the given animal information and name."""
        pass

    @abstractmethod
    def format_animal_list(self, animals_data: str, animal_service_factory) -> str:
        """Format a list of animal data into HTML."""
        pass
