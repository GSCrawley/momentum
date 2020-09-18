class PhysObj:
    def __init__(self, mass, vel):
        """Initialize and set variables"""
        self.mass = mass
        self.vel = vel

    def collide(self, obj2):
        """Calculate the collision with another object"""
        pass

    def calculate_momentum(self, mass, velocity):
        return mass*velocity
