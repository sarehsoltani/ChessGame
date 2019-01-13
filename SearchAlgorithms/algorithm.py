

def path(state):
    solution = []
    cost = state.gn
    while state.parent is not None:
        solution.append(state.entering_action)
        state = state.parent

    solution.reverse()

    print("solution: ", solution)
    print("cost: ", cost)





