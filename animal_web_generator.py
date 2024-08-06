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
    info = '<li class="cards__item">\n'
    if animal.name:
        info += f"Name: {animal.name}<br/>\n"
    if animal.diet:
        info += f"Diet: {animal.diet}<br/>\n"
    if animal.location:
        info += f"Location: {animal.location}<br/>\n"
    if animal.type:
        info += f"Type: {animal.type}<br/>\n"
    info += '</li>\n'
    return info


if __name__ == "__main__":
    main()
