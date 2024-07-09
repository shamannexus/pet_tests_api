import requests


class PetStoreClient:
    def __init__(self, base_url, headers, user_data=None):
        self.base_url = base_url
        self.headers = headers
        self.user_data = user_data

    def create_user(self):
        create_url = f"{self.base_url}/user"
        response_create = requests.post(create_url, headers=self.headers, json=self.user_data)
        assert response_create.status_code == 200
        return self.user_data

    def get_user(self, username):
        get_url = f"{self.base_url}/user/{username}"
        response_get = requests.get(get_url, headers=self.headers)
        assert response_get.status_code == 200
        return response_get.json()

    def get_sold_pets_data(self):
        sold_pets_url = f"{self.base_url}/pet/findByStatus?status=sold"
        response_sold_pets = requests.get(sold_pets_url, headers=self.headers)
        assert response_sold_pets.status_code == 200
        return response_sold_pets.json()

    def get_sold_pets_tuples(self):
        sold_pets_data = self.get_sold_pets_data()
        sold_pets_tuples = [(pet['id'], pet['name']) for pet in sold_pets_data]
        return sold_pets_tuples
