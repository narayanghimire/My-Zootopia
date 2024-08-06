from interface.animal_html_interface import AnimalHTMLInterface
from model.animal import AnimalModel


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

    def read_animal_template(self, template_path) -> str:
        """read animal template and throws error is not found"""
        try:
            with open(template_path, 'r') as template_file:
                return template_file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found: {template_path}")
