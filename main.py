from pet_store_client import PetStoreClient
from pet_name_counter import PetNameCounter

def main():
    base_url = 'https://petstore.swagger.io/v2'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    pet_store_client = PetStoreClient(base_url, headers)
    sold_pets_tuples = pet_store_client.get_sold_pets_tuples()

    pet_name_counter = PetNameCounter(sold_pets_tuples)
    name_counts = pet_name_counter.count_pets_with_same_name()

    print(name_counts)

if __name__ == '__main__':
    main()
