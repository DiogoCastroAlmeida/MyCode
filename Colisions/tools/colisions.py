import sympy as sp
sp.init_printing()


class Equation():
    def __init__(self, first_member, second_member):
        self.first_member = first_member
        self.second_member = second_member

    def __str__(self):
        return f"{self.first_member} = {self.second_member}"


class Colision():


    class Interactor():
        def __init__(self, mass, initial_velocity):
            self.mass = mass
            self.initial_velocity = initial_velocity


    def __init__(self, interactor1, interactor2):
        self.interactor1 = interactor1
        self.interactor2 = interactor2

    def initialize_symbols(self):
        # vf1 -> final velocity of interactor 1
        # vf2 -> final velocity of interactor 2
        self.vf1, self.vf2 = sp.symbols("vf1 vf2")


    def make_momentum_equation(self):
        momentum_equation = (
            self.interactor1.mass*self.interactor1.initial_velocity + self.interactor2.mass*self.interactor2.initial_velocity,
            self.interactor1.mass*self.vf1 + self.interactor2.mass*self.vf2
        )
        self.momentum_equation=sp.Eq(momentum_equation[0], momentum_equation[1])

    def calculate(self):
        self.initialize_symbols()
        self.make_momentum_equation()
        self.make_other_equation()
        self.result = sp.linsolve([self.momentum_equation, self.other_equation], [self.vf1, self.vf2])
        return [self.result.args[0][0].evalf(), self.result.args[0][1].evalf()] 

class ElasticColision(Colision):

    def __init__(self, interactor1, interactor2):
        Colision.__init__(self, interactor1, interactor2)

    def make_other_equation(self):
        other_equation= (
            self.interactor1.initial_velocity + self.vf1,
            self.interactor2.initial_velocity + self.vf2
        )
        self.other_equation = sp.Eq(other_equation[0], other_equation[1])

class InelasticColision(Colision):

    def __init__(self, interactor1, interactor2):
        Colision.__init__(self, interactor1, interactor2)

    def make_other_equation(self):
        other_equation = (
            self.vf1,
            self.vf2
        )
        self.other_equation = sp.Eq(other_equation[0], other_equation[1])

#                       mass, initial__velocity
#a1 = Colision.Interactor(6000, -500)
#a2 = Colision.Interactor(70, -600)

#b = ElasticColision(a1, a2)
#b.initialize_symbols()
#b.make_momentum_equation()
#b.make_other_equation()
#sp.pprint(b.calculate())
