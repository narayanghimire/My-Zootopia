from interface.animal_interface import AnimalInterface
from service.animal_service import AnimalService


def create_animal_service(animal_data) -> AnimalInterface:
    return AnimalService(animal_data)
