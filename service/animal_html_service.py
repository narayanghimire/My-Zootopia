from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from model.animal import AnimalModel
from typing import List, Any, Callable


class AnimalHTMLService(AnimalHTMLInterface):

    def format_animal_info(self, animal: AnimalModel) -> str:
        """Convert animal information to HTML format and return HTML representation of the animal"""
        info = '<li class="cards__item">\n'
        if animal.name:
            info += f'  <div class="card__title">{animal.name}</div>\n'
        info += '  <p class="card__text">\n'
        if animal.location:
            info += f'<strong>Location:</strong> {animal.location}<br/>\n'
        if animal.type:
            info += f'<strong>Type:</strong> {animal.type}<br/>\n'
        if animal.diet:
            info += f'<strong>Diet:</strong> {animal.diet}<br/>\n'
        info += '  </p>\n'
        info += '</li>\n'
        return info

    def format_animal_list(self, animals_data: list, animal_service_factory: Callable[[], AnimalInterface]) -> str:
        """Format a list of animal data into HTML."""
        animal_info = ''
        for animal_data in animals_data:
            animal_service: AnimalInterface = animal_service_factory()
            animal = animal_service.extract_animal_info(animal_data)
            animal_info += self.format_animal_info(animal)
        return animal_info

    def read_animal_template(self, template_path) -> str:
        """read animal template and throws error is not found"""
        try:
            with open(template_path, 'r') as template_file:
                return template_file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found: {template_path}")

    def generate_html(self, animal_info: str, animal_name: str):
        """Generate and save the HTML content."""
        try:
            animal_template_content = self.read_animal_template('resource/animals_template.html')
        except FileNotFoundError as e:
            print(f"Template file not found: {e}")
            return
        except Exception as e:
            print(f"An error occurred while reading the template file: {e}")
            return
        if not animal_info:
            animal_info = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

        new_animal_html_content = animal_template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)
        try:
            with open('animals.html', 'w') as output_file:
                output_file.write(new_animal_html_content)
        except Exception as e:
            print(f"An error occurred while writing the HTML file: {e}")
            return

        print("Animal HTML content written to 'animals.html'.")
