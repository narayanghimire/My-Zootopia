import json
from typing import List, Any

from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from config.config import create_animal_service, create_animal_html_service, create_animal_api_client


def fetch_animal_data(animal_name: str) -> list[Any] | str:
    """Fetch animal data from the API."""
    if not animal_name:
        raise ValueError("Animal name is required")

    animal_client = create_animal_api_client()
    try:
        animals_data = animal_client.fetch_animal_data(animal_name)
    except Exception as e:
        print(f"An error occurred while fetching animal data: {e}")
        return []
    return animals_data


def format_animal_info(animals_data, animal_html_service: AnimalHTMLInterface) -> str:
    """Format animal data into HTML."""
    animal_info = ''
    for animal_data in animals_data:
        animal_service: AnimalInterface = create_animal_service(animal_data)
        animal = animal_service.extract_animal_info()
        animal_info += animal_html_service.format_animal_info(animal)
    return animal_info


def generate_html(animal_html_service: AnimalHTMLInterface, animal_info: str):
    """Generate and save the HTML content."""
    try:
        animal_template_content = animal_html_service.read_animal_template('resource/animals_template.html')
    except FileNotFoundError as e:
        print(f"Template file not found: {e}")
        return
    except Exception as e:
        print(f"An error occurred while reading the template file: {e}")
        return

    new_animal_html_content = animal_template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)
    try:
        with open('animals.html', 'w') as output_file:
            output_file.write(new_animal_html_content)
    except Exception as e:
        print(f"An error occurred while writing the HTML file: {e}")
        return

    print("Animal HTML content written to 'animals.html'.")


def main():
    """Fetch animal data from API, convert it to HTML, and save to a file."""
    animal_html_service: AnimalHTMLInterface = create_animal_html_service()
    animal_name = input("Enter the name of the animal you want to search for: ").strip()

    if not animal_name:
        print("Animal name cannot be empty.")
        return

    try:
        animals_data = fetch_animal_data(animal_name)
    except ValueError as e:
        print(e)
        return

    if not animals_data:
        print("No data found for the given animal.")
        return

    animal_info = format_animal_info(animals_data, animal_html_service)
    generate_html(animal_html_service, animal_info)


if __name__ == "__main__":
    main()
