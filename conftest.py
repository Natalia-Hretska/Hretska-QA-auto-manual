import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.nova_poshta_page import NovaPoshtaPage
from modules.ui.page_objects.rozetka_cart_page import RozetkaCartPage

class User():

    def __init__(self):
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = "Natalia"
        self.second_name = "Hretska"
    
    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    
    yield api

@pytest.fixture
def database():
    db = Database()

    yield db


@pytest.fixture
def rozetka_cart_page():
    rozetka_cart_page = RozetkaCartPage() 

    yield rozetka_cart_page   


@pytest.fixture
def nova_poshta_page():
    nova_poshta_page = NovaPoshtaPage()

    yield nova_poshta_page