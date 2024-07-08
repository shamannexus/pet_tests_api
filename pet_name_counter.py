class PetNameCounter:
    def __init__(self, pets_data):
        self.pets_data = pets_data

    def count_pets_with_same_name(self):
        name_counts = {}
        for pet_id, pet_name in self.pets_data:
            if pet_name in name_counts:
                name_counts[pet_name] += 1
            else:
                name_counts[pet_name] = 1
        # Sort the name_counts_data dictionary by count in descending order and return a list of tuples
        sorted_name_counts = sorted(name_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_name_counts
