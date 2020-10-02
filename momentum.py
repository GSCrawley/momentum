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
        Velocity after collision: {self.velF}gi
        momentum after collision: {self.momentumFinal}'''

    def collide(self, obj2):
        """Calculate the elastic collision with another object, assume object 2 travels in opposite direction"""
        # Pi = Pf => m1V1i + m2V2i = m1V1f + m2V2f
        pi = self.momentumInital + obj2.momentumInital

        #V1f + V1i = V2i + V2f => V1f = V2f + (V2i-V1i)
        initials = obj2.velI - self.velI
        #V2f = Pi-m1(initals)/(m1+m2)
        obj2.velF = (pi-self.mass*initials)/(self.mass+obj2.mass)

        #V1f = V2f + (V2i-V1i)
        self.velF = obj2.velF + initials

        obj2.momentumFinal = self._calculate_momentum(obj2.mass, obj2.velF)
        self.momentumFinal = self._calculate_momentum(self.mass, self.velF)


    def _calculate_momentum(self, mass, vel):
        """Helper function to determine momentum"""
        # p = m*v
        return mass * vel


if __name__ == '__main__':
    mass1_input = input("Enter your first object's mass (kg): ")
    vel1_input = input("Enter your first object's velocity (m/s): ")

    #make sure you make the  velocity negative as we assume object is traveling opposite to object 1
    mass2_input = input("Enter your second object's mass (kg): ")
    vel2_input = input("Enter your second object's velocity (m/s): ")

    obj1 = PhysObj(mass1_input, vel1_input, 1)
    obj2 = PhysObj(mass2_input, vel2_input, 2)

    obj1.collide(obj2)

    print(obj1.__str__())
    print(obj2.__str__())