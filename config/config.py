from interface.animal_client_interface import AnimalClientInterface
from interface.animal_html_interface import AnimalHTMLInterface
from interface.animal_interface import AnimalInterface
from service.animal_html_service import AnimalHTMLService
from service.animal_service import AnimalService
from service.animal_api_client import AnimalApiClient
from utils.singleton import singleton


@singleton
def create_animal_service() -> AnimalInterface:
    """Create the instance of animal service and return the interface as instance of AnimalInterface"""
    animal_client = create_animal_api_client()
    return AnimalService(animal_client)


@singleton
def create_animal_html_service() -> AnimalHTMLInterface:
    """create the instance of animal html service and return the interface as instance of AnimalHTMLService"""
    return AnimalHTMLService()


@singleton
def create_animal_api_client() -> AnimalClientInterface:
    """Create an instance of AnimalApiClient and return it as an AnimalClientInterface."""
    return AnimalApiClient()
