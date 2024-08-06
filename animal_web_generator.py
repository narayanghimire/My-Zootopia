from config.config import create_animal_service, create_animal_html_service
from interface.animal_html_interface import AnimalHTMLInterface


def main():
    """Fetch animal data from API, convert it to HTML, and save to a file."""
    animal_html_service: AnimalHTMLInterface = create_animal_html_service()
    animal_name = input("Enter the name of the animal you want to search for: ").strip()

    if not animal_name:
        print("Animal name cannot be empty.")
        return

    try:
        animals_data = create_animal_service().fetch_animal_data(animal_name)
    except ValueError as e:
        print(e)
        return

    animal_info = animal_html_service.format_animal_list(animals_data, create_animal_service)
    animal_html_service.generate_html(animal_info, animal_name)


if __name__ == "__main__":
    main()
