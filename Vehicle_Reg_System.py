# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle():
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"{self.owner} is the new owner of a {self.type} with the registration number of {self.registration_number}.")
    


john = Vehicle('12345678', 'Sedan', 'John Brown')
bob = Vehicle('98765432', 'Van', 'Bob Berts')


john.update_owner('George Straight')
bob.update_owner('Melissa Johnson')
