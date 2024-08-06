import json
from interface.animal_interface import AnimalInterface
from config.config import create_animal_service


def main():
    with open('resource/animals_data.json') as f:
        animals_data = json.load(f)

        for animal_data in animals_data:
            animal_service: AnimalInterface = create_animal_service(animal_data)
            animal = animal_service.extract_animal_info()
            animal_service.display_animal_info(animal)


if __name__ == "__main__":
    main()
