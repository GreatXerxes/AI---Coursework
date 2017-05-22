import random

def dist(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))     # L_inf

########################################################################

class Klingon:
    klingon_range = 10
    def __init__(self):
        self.x = random.randrange(self.klingon_range)
        self.y = random.randrange(self.klingon_range)

    def move(self):
        pass                            # basic klingon does not move in core task

    def estimated_by(self, ship):
        ship.measure(dist(self.x, self.y,
                          ship.x, ship.y))

    def found_by(self, ship):
        return dist(self.x, self.y, ship.x, ship.y) == 0

    def __repr__(self):
        return "Klingon is at %d,%d" % (self.x, self.y)

########################################################################

class Ship:
    def __init__(self, xklingon, yklingon):
        self.x_range = xklingon
        self.y_range = yklingon
        
        # this is the a priori probability
        p_w = {}
        for x in range(xklingon):
            for y in range(yklingon):
                p_w[x,y] = 1/99          # fill in expression

        self.p_w = p_w

        self.x = random.randrange(self.x_range)
        self.y = random.randrange(self.y_range)

    # characteristics of distance measure: p(d|x,y) where x,y is a
    # possible position of the klingon (remember the mine problem)

    def p_d_cond_w(self, d, x, y):
        if dist(x, y, self.x, self.y) == d:
            return 1
        else:
            return 0
        # fill in probability p(d|x,y) of finding a distance d if x,y
        # is the position of the klingon. Note that ship has access to
        # its own position via self.x and self.y

    def measure(self, d):
        # for each possible position w=x,y of the klingon
        # calculate p(w|d)

        p_w_cond_d = {}
        # new probabilities for klingon position, if distance 'd' has
        # been measured: p(w|d) = p(d|w) p(w)

        for x in range(10):
            for y in range(10):
                Z = sum(self.p_d_cond_w(d,x,y) * self.p_w[x,y] for x, y in self.p_w)
                print "Z is ", Z
                if Z <> 0:
                    for x in range(self.x_range):
                        for y in range(self.y_range):
                            self.p_w_cond_d[x, y]/= Z

                    self.p_w = self.p_w_cond_d
        # fill in the Bayesian formula for calculating p_w_cond_d, i.e. p(w|d)


    def show_model(self):# Two ways of printing the grid..... the one uncommented looks better but both work
        grid = [[self.p_w for i in range(10)] for j in range(10)]
        #grid = [[self.p_w[self.x, self.y] for i in range(10)] for j in range(10)]

        print grid



       # for y in range(10):
       #     print ""
       #     for x in range(10):
        #        print "[" + str(round(self.p_w[x,y], 2)) + "]"


        # fill in a print routine printing the current Bayesian model
        # p(w|d) where w is the klingon position (x,y)

    def move(self): # randomly sets the ship
        new_x = random.randrange(0, 10, 1)
        new_y = random.randrange(0, 10, 1)

        new_values = []
        new_values.append(max(self.p_w))

        print "New Value: " + str(new_values)
        ship.x = new_x
        ship.y = new_y

        ship.x = new_values[0]
        #ship.y = new_values[1]
        # fill in a ship's move. Begin with random jumps, for simplicity

    def __repr__(self):
        return "Ship at %d,%d" % (self.x, self.y) # pretty print

########################################################################

def run(klingon, ship):
    while not klingon.found_by(ship):
        raw_input()
        klingon.move()
        klingon.estimated_by(ship)            # ship gets distance

        ship.show_model()                   # show current Bayesian model
        ship.move()                         # to be filled in
        print ship
    print "Klingon found"

klingon = Klingon()
ship = Ship(klingon.klingon_range, klingon.klingon_range)
run(klingon, ship)


    
