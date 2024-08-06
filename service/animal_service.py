from interface.animal_interface import AnimalInterface
from model.animal import AnimalModel


class AnimalService(AnimalInterface):
    def __init__(self, animal_data):
        self.animal_data = animal_data

    def extract_animal_info(self) -> AnimalModel:
        name = self.animal_data.get("name")
        characteristics = self.animal_data.get("characteristics", {})
        diet = characteristics.get("diet")
        locations = self.animal_data.get("locations", [])
        location = locations[0] if locations else None
        type_ = characteristics.get("type")

        return AnimalModel(name, diet, location, type_)

    def display_animal_info(self, animal: AnimalModel):
        if animal.name:
            print(f"Name: {animal.name}")
        if animal.diet:
            print(f"Diet: {animal.diet}")
        if animal.location:
            print(f"Location: {animal.location}")
        if animal.type:
            print(f"Type: {animal.type}")
        print()


