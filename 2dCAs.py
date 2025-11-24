import pygame
import numpy as np
#from itertools import product

class TwoDCellularAutomaton:
    def __init__(self, grid_dim, initial_conditions=[], rule='game_of_life', WIDTH=None, HEIGHT=None, TILE_SIZE=None, FPS=None):
        self.grid_dim = grid_dim
        self.initial_conditions = initial_conditions
        self.rule = rule
        #self.visualization = visualization
        self.grid = self.init_grid()

        self.WIDTH = 600 if WIDTH == None else WIDTH 
        self.HEIGHT = 600 if HEIGHT == None else HEIGHT
        self.TILE_SIZE =  20 if TILE_SIZE == None else TILE_SIZE
        self.FPS = 60 if FPS == None else FPS
        


    def init_grid(self):
        grid = np.zeros((self.grid_dim, self.grid_dim), dtype=np.uint8)
        #print(f"init conditions: {self.initial_conditions}")
        for dims in self.initial_conditions:
            x = dims[0]
            y = dims[1]
            grid[x][y] = 1
        
        return grid

    
    def apply_rule(self, i, j):
        if self.rule == "game_of_life":
            """ The game of life is based on the number of neighbours alive
                if the cell is alive and the sum of the neighbours is either 0 and 1, or 4 or more, the cell dies
                if the cell is not alive and the sum of the neighbours is 3, the cell turns to be alive
                else the cell keeps the same (based on the webpage I saw, lol)
            """
            neighborSum = 0

            for rowNeighbors in range(-1, 2):
                for columnNeighbors in range(-1, 2):
                    neighborSum += self.grid[rowNeighbors][columnNeighbors]
            

            neighborSum -= self.grid[i][j]

            if self.grid[i][j] == 1 and neighborSum < 2: return 0
            elif self.grid[i][j] == 1 and neighborSum > 3: return 0
            elif self.grid[i][j] == 0 and neighborSum == 3: return 1
            else: return self.grid[i][j]

        else:
            pass


    def evolution(self):
        next_state = np.zeros((self.grid_dim, self.grid_dim), dtype=np.int8)

        """
        Im going to avoid applying the rule on edges (to save computational cost, 
        you know, the program will crash on -1 and n=grid_dim-1, so a "def check" function is needed)
        obviously, not the complete implementation, considering how I am, lol
        change it in the future to consider edges as well
        """
        # Applying the rule to each cell in the current state 
        for row in range(1, self.grid_dim-1): # Avoiding edges
            for column in range(1, self.grid_dim-1): # Avoiding edges as well
                next_state[row][column] = self.apply_rule(row, column)
        
        print(f"next state: {next_state}")
        
        return next_state
    

    def visualization(self):
        """
        freaking boring, going to sleep, chaops!
        """
        pass

        

    """
    This is only if you want to choose the initial conditions manually, I will try to set it up visually using pygame
    def check_init_conditions(self):
        for row in range(self.grid_dim):
            for column in range(self.grid_dim):
                if self.grid[row][column] == 1:
                    print(f"black cell in {row},{column}")
                    return
    """


# initial conditions are tuples indicating the coordenates where the cells are black
gameOfLife = TwoDCellularAutomaton(grid_dim=100, initial_conditions=[(50, 50)], rule="game_of_life")

gameOfLife.evolution()


