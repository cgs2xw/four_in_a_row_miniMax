from GameState import GameState 
import copy

##https://anytree.readthedocs.io/en/latest/index.html##
from anytree import Node, RenderTree

class Player(object):
    def __init__(self, name):
        self.name = name


    def generate_move(self, current_state, value, depth):
        #minimax function
        bestState = None
        best_eval = -10000000000
        startNode = self.create_gametree(current_state, depth, value) # creation of the tree
        if value == 'x':      # looking for best eval in the next level down
            for child in startNode.children:
                if child.name.eval[0] > best_eval:
                    bestState = child.name
                    best_eval = child.name.eval[0]
           
        if value == 'o': # looking for best eval in the next level down
            for child in startNode.children:
                if child.name.eval[1] > best_eval:
                    bestState = child.name
                    best_eval = child.name.eval[1]
        return bestState  

    def create_gametree(self, current_state: GameState, depth, value,starting_node = None, pruneMax= None):
        if not starting_node:
            starting_node = Node(current_state)

        if not pruneMax:
            pruneMax = -10000000000000 if depth % 2 != 0 else 1000000000000

        evalNumber = -10000000000000 if depth % 2 == 0 else 1000000000000
        bestEval = -10000000000000 if depth % 2 == 0 else 1000000000000

        for available_move in current_state.find_playable():
            new_state = copy.deepcopy(current_state)
            notValue = 'o' if value == 'x' else 'x'

            if depth%2 == 0: # max player setting the move
                new_state.set(available_move[0], available_move[1], value)
            else: # min player making a move
                new_state.set(available_move[0], available_move[1], notValue)
            #new_state.printAll()
            #print("")
            new_node = Node(new_state, parent = starting_node) #stting the node for the min or max

            if depth > 1: #if we haven't gone far enough down recall the function and do some evaluations to pick the best option and set that to eval
                childEval = self.create_gametree(new_state, depth - 1, value, new_node, pruneMax).name.eval
                if value == 'x': 
                    if depth % 2 == 0: ## if max and the eval is greater for this child than the previous greatest set the eval to it for x
                        if childEval[0] > evalNumber:
                            evalNumber = childEval[0]
                        if childEval[0] < pruneMax:
                            continue
                    else: ## min
                        if childEval[0] < evalNumber: 
                            evalNumber = childEval[0]
                        if childEval[0] > pruneMax:
                            continue
                    starting_node.name.eval[0] = evalNumber
                elif value == 'o': # if max and eval is ess than the eval but for o
                    if depth % 2 == 0:
                        if childEval[1] > evalNumber:
                            evalNumber = childEval[1]
                        if childEval[1] < pruneMax:
                            continue
                    else: ## min
                        if childEval[1] < evalNumber: 
                            evalNumber = childEval[1]
                        if childEval[1] > pruneMax:
                            continue
                    starting_node.name.eval[1] = evalNumber
            pruneMax = starting_node.name.eval[0] if value == 'x' else starting_node.name.eval[1]
        return starting_node

    def print_tree(self, start_node):
        for pre, fill, node in RenderTree(start_node):
            print("%s%s" % (pre, node.name))









