from GameState import GameState 

##https://anytree.readthedocs.io/en/latest/index.html##
from anytree import Node, RenderTree

class Player(object):
    def __init__(self, name):
        self.name = name


    def generate_move(self, current_state):
        pass
            #minimax function

    def create_gametree(self, current_state: GameState, depth, starting_node = None):
        if not starting_node:
            starting_node = Node(current_state)
        for available_move in current_state.find_playable():
            new_state = GameState(current_state)
            new_state.set(available_move[0], available_move[1], 'x')
            new_node = Node(new_state, parent = starting_node)
            self.print_tree(starting_node)
            if depth > 1:
                self.create_gametree(new_state, depth - 1, new_node)
        return starting_node

    def print_tree(self, start_node):
        for pre, fill, node in RenderTree(start_node):
            print("%s%s" % (pre, node.name))









