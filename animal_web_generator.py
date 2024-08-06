import json
from interface.animal_interface import AnimalInterface
from config.config import create_animal_service


def main():
    with open('resource/animals_data.json') as f:
        animals_data = json.load(f)

        animal_info = ''
        for animal_data in animals_data:
            animal_service: AnimalInterface = create_animal_service(animal_data)
            animal = animal_service.extract_animal_info()
            animal_info += format_animal_info(animal)
    with open('resource/animals_template.html', 'r') as template_file:
        template_content = template_file.read()
    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)
    with open('animals.html', 'w') as output_file:
        output_file.write(new_html_content)


def format_animal_info(animal):
    info = ""
    if animal.name:
        info += f"<li>Name: {animal.name}</li>\n"
    if animal.diet:
        info += f"<li>Diet: {animal.diet}</li>\n"
    if animal.location:
        info += f"<li>Location: {animal.location}</li>\n"
    if animal.type:
        info += f"<li>Type: {animal.type}</li>\n"
    info += "<br>\n"
    return info


if __name__ == "__main__":
    main()
