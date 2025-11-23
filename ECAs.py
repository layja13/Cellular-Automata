# Elementary Cellular Automatas
# Grid? lol

from itertools import product
import numpy as np
import matplotlib.pyplot as plt

class ElementaryCellularAutomaton:
    def __init__(self, initial_conditions=[0,0,0], rule=0):
        self.initial_conditions = np.asarray(initial_conditions)
        self.current_state = list(initial_conditions)
        if self.current_state[-1] == 1: self.current_state.append(0)
        if self.current_state[0] == 1: self.current_state.insert(0, 0)   # I dont know how efficient is this one
        self.current_state = np.asanyarray(self.current_state)

        # We use this array to save each state of the CA 
        self.evolution_history = []

        # The rule is a decimal number - should be from 256 to 0
        self.rule = rule

        # We convert the decimal number in an 8 bits binary number
        self.rule_binary = self.decimal_2_binary(rule)

        """ We stablish the possible states of the CA in triples, which are the combinatorics of 0 and 1 in triples.
         The possible states are always - [1 1 1], [1 1 0], [1 0 1], [1 0 0], [0 1 1], [0 1 0], [0 0 1], [0 0 0] 
        """
        possible_conditions = product((1,0), repeat=3)

        """
         We assign the rules
         We have 8 possible states [1 1 1], [1 1 0], [1 0 1], [1 0 0], [0 1 1], [0 1 0], [0 0 1], [0 0 0]
         We also have an 8 bits binary number based on the rule which is decimal number
         Each possible state will have a next state based on the 8 bits binary number 
        """
        
        self.rules = {p: self.rule_binary[i] for i, p in enumerate(possible_conditions)}

        self.step = 1


    # ECAs have 8 possible bits at most in their initial conditions, so this method start from 256 possible decimal numbers
    def decimal_2_binary(self, num):
        ans = []
        start = 256

        while start > 1:
            start //= 2
            if num >= start:
                ans.append(1)
                num -= start
            else:
                ans.append(0)
        return ans
    

    def evolution(self, steps_target):

        """ Filling the first state with the same amount of cells as the final number of cells in the last state
            This is important to be able to plot the CA in matplotlib, as it requires an square matrix
        """ 
        length_initial_conditions = len(self.initial_conditions)
        length_final_state = (steps_target*2) # ECAs increase by two in each step
        to_add = (length_final_state - length_initial_conditions)/2

        # We add one zero o each side, or one zero more to the right side if the number of zeros to add is impair
        if to_add  % 2 == 0:
            to_add_first = to_add
            to_add_second = to_add - 1
        else:
            to_add_first = int(np.floor(to_add))
            to_add_second = int(np.ceil(to_add) - 1)
        
        self.evolution_history.append(np.concatenate((np.zeros((int(to_add_first+1),), dtype=int), self.current_state, np.zeros((int(to_add_second+1),), dtype=int))))


        """ This is where the magic happen, lol, ok just joking
            the evolution starts
        """
        while self.step < steps_target:
            #print(self.current_state)

            
            """
            We add the current state in the array that will contain all the states of the evolution
            We concatenate the number of 0 in both left and right sides to make an square matrix to plot it using matplotlib
            """
            add_left_right_current_state = self.evolution_history[self.step-1][0]
            add_left_right_next_state = self.rules[(add_left_right_current_state, add_left_right_current_state, add_left_right_current_state)]
            next_state = [add_left_right_next_state]
            
            """ 
            The first triple to evaluate 
            """
            left_cell = add_left_right_current_state
            middle_cell = self.current_state[0]
            right_cell = self.current_state[1]

            next_state.append(self.rules[(left_cell, middle_cell, right_cell)])

            for i in range(1, len(self.current_state)-1):
                """
                We evaluate the triples and apply the rule one by one of the whole state in this step of time
                """
                left_cell = self.current_state[i-1]
                middle_cell = self.current_state[i]
                right_cell = self.current_state[i+1]

                next_state.append(self.rules[(left_cell, middle_cell, right_cell)])


            left_cell = self.current_state[-2]
            middle_cell = self.current_state[-1]
            right_cell = add_left_right_current_state

            next_state.append(self.rules[(left_cell, middle_cell, right_cell)])
            next_state.append(add_left_right_next_state)

            self.current_state = next_state     

            if add_left_right_next_state == 0:
                self.evolution_history.append(np.concatenate((np.zeros((int(to_add_first),), dtype=int), self.current_state, np.zeros((int(to_add_second),), dtype=int))))
            else:
                self.evolution_history.append(np.concatenate((np.ones((int(to_add_first),), dtype=int), self.current_state, np.ones((int(to_add_second),), dtype=int))))

            to_add_first -= 1
            to_add_second -= 1       
 
            self.step += 1

        self.step = 1

        plt.figure(figsize=(10, 6))
        plt.imshow(self.evolution_history, interpolation='nearest', cmap='gray_r', aspect='auto', origin='upper')
        plt.ylabel("time step")
        plt.title(f"Cellular Automaton. Rule {self.rule}")
        plt.tight_layout()
        plt.show()

        return next_state


"""
Philosophical questions
preguntarte porqué tiene que tomar en cuenta las white celdas de los costados
"""

class TwoDCellularAutomaton:
    def __init__(self):
        pass
    