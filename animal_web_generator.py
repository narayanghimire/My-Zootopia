import json

from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from config.config import create_animal_service, create_animal_html_service, create_animal_api_client


def fetch_animal_data() -> str:
    """Fetch animal data from the API."""
    animal_name = 'Fox'
    animal_client = create_animal_api_client()
    return animal_client.fetch_animal_data(animal_name)


def format_animal_info(animals_data, animal_html_service) -> str:
    """Format animal data into HTML."""
    animal_info = ''
    for animal_data in animals_data:
        animal_service: AnimalInterface = create_animal_service(animal_data)
        animal = animal_service.extract_animal_info()
        animal_info += animal_html_service.format_animal_info(animal)
    return animal_info


def generate_html(animal_html_service, animal_info):
    """Generate and save the HTML content."""
    try:
        animal_template_content = animal_html_service.read_animal_template('resource/animals_template.html')
    except FileNotFoundError as e:
        print(e)
        return

    new_animal_html_content = animal_template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)
    with open('animals.html', 'w') as output_file:
        output_file.write(new_animal_html_content)

    print("Animal HTML content written to 'animals.html'.")


def main():
    """Fetch animal data from API, convert it to HTML, and save to a file."""
    animal_html_service: AnimalHTMLInterface = create_animal_html_service()
    animals_data = fetch_animal_data()
    if not animals_data:
        print("No data found for the specified animal.")
        return
    animal_info = format_animal_info(animals_data, animal_html_service)

    generate_html(animal_html_service, animal_info)


if __name__ == "__main__":
    main()
