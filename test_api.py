import pytest
import random
import string
from pet_store_client import PetStoreClient


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture
def headers():
    return {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }


@pytest.fixture
def random_string():
    """Generate a random string of fixed length"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))


@pytest.fixture
def user_data(random_string):
    return {
        "id": 0,
        "username": f"test_user_{random_string}",
        "firstName": "Test_user_first_name",
        "lastName": "Test_user_last_name",
        "email": f"text_user_{random_string}@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 0
    }


def test_create_user_and_verify_fields(base_url, headers, user_data):
    pet_store_client = PetStoreClient(base_url, headers, user_data)

    created_user_data = pet_store_client.create_user()

    # Verify user fields
    assert created_user_data['username'] == user_data['username']
    assert created_user_data['email'] == user_data['email']
    assert created_user_data['firstName'] == user_data['firstName']
    assert created_user_data['lastName'] == user_data['lastName']
    assert created_user_data['phone'] == user_data['phone']
    assert created_user_data['userStatus'] == user_data['userStatus']


def test_fetch_sold_pets_and_verify_format(base_url, headers):
    pet_store_client = PetStoreClient(base_url, headers)
    sold_pets_data = pet_store_client.get_sold_pets_data()

    # Verify the format of each pet in the list
    for pet in sold_pets_data:
        assert 'id' in pet
        assert 'name' in pet

    assert len(sold_pets_data) > 0
