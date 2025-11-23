from ECAs import ElementaryCellularAutomaton

eca = ElementaryCellularAutomaton(initial_conditions=[0, 1, 0], rule = 149)

eca.evolution(steps_target=16)



