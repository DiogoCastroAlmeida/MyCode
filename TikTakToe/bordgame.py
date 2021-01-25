class Space():


    def __init__ (self, filled=False, owner=None):
        self.filled = filled
        self.owner = owner


    def fill(self, player):
        self.filled = True
        self.owner = player

#a = Space
#print(a)

class BordGame():


    def gen_bord(self):
        self.bord = []
        for y in range(self.layout[1]) :
            self.bord.append( [Space() for x in range(self.layout[0])])


    def __init__(self, layout): #layout has to be a tuple with the format (x, y)
        self.layout = layout
        self.gen_bord()
    

#bord = BordGame((3, 2))
##print(bord.bord)
#print(bord.bord[0][0].owner)    

    