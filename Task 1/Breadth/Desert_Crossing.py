########################################################################
# Desert Crossing (version for use with breadth first search)
########################################################################

from copy import deepcopy

#def valid

class Desert_Crossing:

    def start(self):
        #the number on the first cell of tuple is a heuristic based on
        #total number of fuel in left base
        return (99, { 'home' : {'Fuel' : 99},
                      '1st' : {'Fuel' : 0},
                      '2nd' : {'Fuel' : 0},
                      '3rd' : {'Fuel' : 0},
                      'goal' : {'Fuel' : 0},
                      'truck' : 'home'})

    def goal(self, state):
        statedict=state[1]
        return statedict['goal'] == {'truck' : 'goal'}

    def succ(self, state):
        other_base = {'home' : '1st', '1st': '2nd', '2nd' : '3rd', '3rd' : 'goal',
                       'goal' : '3rd', '3rd' : '2nd', '2nd' : '1st', '1st' : 'home'}
        max_truck = 3 #Max amount of fuel truck can hold
        statedict = state[1]
        active_base = statedict['truck']
        fuel = statedict[active_base]['Fuel']

        succlist = []

        for total_fuel in range(1, max_truck+1):# how many fuel cans to take
            for fuel_trav in range(1, total_fuel+1):

                new_statedict = deepcopy(statedict)

                new_statedict[active_base]['Fuel'] = statedict[active_base]['Fuel'] - fuel_trav

                new_statedict['truck'] = other_base[statedict['truck']]

                new_statedict[other_base[active_base]]['Fuel'] = statedict[other_base[active_base]]['Fuel'] + fuel_trav - 1
                new_state=
        return succlist
    
                
