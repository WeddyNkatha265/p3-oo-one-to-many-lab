# class Pet:

#     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
#     all = []
#     def __init__(self, name, pet_type, owner=None):
#         self.name = name
#         self.pet_type = pet_type
#         self.owner = owner

#     if __name__ == "__main__":
#         print(Pet.PET_TYPES)
#         raise Exception    

# class Owner:

#     def __init__(self, name):
#         self.name = name
#         self.pets = []

#     def pets(self):
#         return self.pets.copy()    

#     def add_pet(self, pet):
#         self.pets.append(pet)

#         if not isinstance(pet, Pet):
#             raise Exception("Pet must be an instance of Pet class")

#     def get_sorted_pets(self):
#         return sorted(self.pets, key=lambda x: x.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

