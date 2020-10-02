class PhysObj:
    """Class for objects to be used in calculations"""

    def __init__(self, mass, vel, id=0):
        """Initialize and set variables"""
        self.id = id
        self.mass = float(mass)
        self.velI = float(vel)
        self.momentumInital = self._calculate_momentum(self.mass,  self.velI)
        self.velF = float(0)
        self.momentumFinal = float(0)

    def __str__(self):
        """Dunder to output information on the object"""
        return f'''Object {self.id}:
        Mass: {self.mass}
        Velocity after collision: {self.vel}\n'''

    def collide(self, obj2):
        """Calculate the elastic collision with another object, assume object 2 travels in opposite direction"""
        # Pf = Pi

        #V1f + V1i = V2i + V2f 
        self.velfF = (self.mass-obj2.mass)/(self.mass+obj2.mass)
        self.velF = self.velF*self.velI

        obj2.velF = self.velF + self.velI - obj2.velI

        obj2.momentumFinal = self._calculate_momentum(obj2.mass, obj2.velF)
        self.momentumFinal = self._calculate_momentum(self.mass, self.velF)

        # if self.vel > obj2.vel:
        #     # a = F/m
        #     self.vel -= total_force / self.mass
        #     obj2.vel += total_force / obj2.mass
        # elif self.vel < obj2.vel:
        #     self.vel += total_force / self.mass
        #     obj2.vel -= total_force / obj2.mass
        # else:
        #     print("No collision")

    def _calculate_momentum(self, mass, vel):
        """Helper function to determine momentum"""
        # p = m*v
        return mass * vel


if __name__ == '__main__':
    mass1_input = input("Enter your first object's mass (kg): ")
    vel1_input = input("Enter your first object's velocity (m/s): ")

    mass2_input = input("Enter your second object's mass (kg): ")
    vel2_input = input("Enter your second object's velocity (m/s): ")

    obj1 = PhysObj(mass1_input, vel1_input, 1)
    obj2 = PhysObj(mass2_input, vel2_input, 2)

    obj1.collide(obj2)

    print(obj1)
    print(obj2)
