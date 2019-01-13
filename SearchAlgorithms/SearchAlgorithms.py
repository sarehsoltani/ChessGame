import sys

class SearchAlgorithms(object):
    """description of class"""
    def __init__(self, problem):
        self.problem = problem

    def TBFS(self,start_state):
        queue = list((start_state))  # nodes_to_expand
        AllocatedMemory = 0
        Number_of_expanded_nodes = 0
        path = []
        
        while (len(queue)>0):   
            current_state = queue.pop(0)
            path.append(current_state)
            Number_of_expanded_nodes += 1
            if self.problem.isGoalTest(current_state):
                print("**Tree breathFirstSearch Algorithms**")
                print("Number Of Expanded Nodes:" + str(Number_of_expanded_nodes))
                print("Number Of Visited Nodes:" + str(Number_of_expanded_nodes))
                print("Final State:" + str(current_state))                
                print("Allocated Memory" + str(AllocatedMemory))
                self.tree_print_path(path)
                return current_state
            states = self.problem.results(self.problem.actions(current_state), current_state)
            for state in states:
                queue.append(state)
                AllocatedMemory += 1
        

    def print_path(self, leaf_node):
        path = []
        while leaf_node:
            path.append(leaf_node)
            if leaf_node in self.parent:
                leaf_node = self.parent[leaf_node]
            else:
                leaf_node = None
        self.problem.print_path(list(reversed(path)))

    def print_path_from_goal(self, leaf_node):
        print("From goal")
        path = []
        while leaf_node:
            path.append(leaf_node)
            if leaf_node in self.parent_from_goal:
                leaf_node = self.parent_from_goal[leaf_node]
            else:
                leaf_node = None
        self.problem.print_path(list(reversed(path)))

    def tree_print_path(self, path):
        self.problem.print_path(list(path))
        for item in path:
            print(item)

