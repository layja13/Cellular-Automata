# Elementary Cellular Automatas
# Grid? lol

from itertools import product
import numpy as np
import matplotlib.pyplot as plt

class ElementaryCellularAutomaton:
    def __init__(self, initial_conditions=[0,0,0], rule=0):
        self.initial_conditions = np.asarray(initial_conditions)
        self.current_state = np.asarray(initial_conditions)
        if self.current_state[-1] == 1: self.current_state = np.append(self.current_state, 0)
        if self.current_state[0] == 1: self.current_state = np.insert(self.current_state, 0, 0)   # I dont know how efficient is this one

        self.evolution_history = []

        self.rule = rule
        self.rule_binary = self.decimal_2_binary(rule)

        possible_conditions = product((1,0), repeat=3)
        self.rules = {p: self.rule_binary[i] for i, p in enumerate(possible_conditions)}

        self.step = 1

    # ECAs have 8 possible bits at most in their initial conditions

    def decimal_2_binary(self, num):
        ans = np.empty(shape=1, dtype=bool)
        start = 256

        while start > 1:
            start /= 2
            if num >= start:
                ans = np.append(ans, 1)
                num = num - start
            else:
                ans = np.append(ans, 0)

        return ans
    

    def evolution(self, steps_target):
        while self.step < steps_target:
            #print(self.current_state)
            self.evolution_history.append(self.current_state)
            next_state = np.asarray([0])
            left_cell = 0
            middle_cell = self.current_state[0]
            right_cell = self.current_state[1]

            next_state = np.append(next_state, self.rules[(left_cell, middle_cell, right_cell)])

            for i in range(1, len(self.current_state)-1):
                left_cell = self.current_state[i-1]
                middle_cell = self.current_state[i]
                right_cell = self.current_state[i+1]

                next_state = np.append(next_state, self.rules[(left_cell, middle_cell, right_cell)])

            left_cell = self.current_state[-2]
            middle_cell = self.current_state[-1]
            right_cell = 0

            next_state = np.append(next_state, self.rules[(left_cell, middle_cell, right_cell)])
            next_state = np.append(next_state, 0)


            self.current_state = next_state            
 
            self.step += 1

        self.step = 1


        print(f"{self.evolution_history}")

        #plt.rcParams['image.cmap'] = 'binary'
        #fig, ax = plt.subplots(figsize=(16,9))
        #ax.matshow(self.evolution_history)
        #ax.axis(False)

        return next_state


ca = ElementaryCellularAutomaton(initial_conditions=[0,1,0], rule=110)

#print(ca.rule)
#print(ca.rule_binary)
#print(ca.rules)

ca.evolution(steps_target=20)

# Next steps 
# 1. visualizarlo en matplotlib
# preguntarte porqué tiene que tomar en cuenta las white celdas de los costados?
