mass_input = input("Enter your object's mass: ")
vel_input = input("Enter your object's velocity: ")

class PhysObj:
    def __init__(self, mass, vel):
        """Initialize and set variables"""
        self.mass = mass
        self.vel = vel

    def collide(self, obj2):
        """Calculate the collision with another object"""
        pass

    def calculate_momentum(self):
        return self.mass*self.vel

   