from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from service.animal_html_service import AnimalHTMLService
from service.animal_service import AnimalService


def create_animal_service(animal_data) -> AnimalInterface:
    return AnimalService(animal_data)


def create_animal_html_service() -> AnimalHTMLInterface:
    return AnimalHTMLService()
