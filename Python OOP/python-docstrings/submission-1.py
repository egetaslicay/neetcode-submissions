class Pet:
    """
    A class to represent a pet 

    Attributes: 
    name (str): Pet's name
    animal_type (str): type of animal the pet is 

    """ 


    def __init__(self, name: str, animal_type: str):
        """ Initialize a new pet instance """ 
        self.name = name
        self.animal_type = animal_type

    def make_sound(self) -> str:
        """ Returns a sound depending on the type of animal the pet is no args """ 
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)

