import json

from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from config.config import create_animal_service
from config.config import create_animal_html_service


def main():
    """Load animal data, convert it to HTML, and save to a file."""
    animal_html_service: AnimalHTMLInterface = create_animal_html_service()
    with open('resource/animals_data.json') as f:
        animals_data = json.load(f)

        animal_info = ''
        for animal_data in animals_data:
            animal_service: AnimalInterface = create_animal_service(animal_data)
            animal = animal_service.extract_animal_info()
            animal_info += animal_html_service.format_animal_info(animal)
    try:
        animal_template_content = animal_html_service.read_animal_template('resource/animals_template.html')
    except FileNotFoundError as e:
        print(e)
        return

    new_animal_html_content = animal_template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)
    with open('animals.html', 'w') as output_file:
        output_file.write(new_animal_html_content)

    print("Animal html content written to 'animals.html'.")


if __name__ == "__main__":
    main()
