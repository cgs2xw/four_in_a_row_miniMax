from GameState import GameState 

##https://anytree.readthedocs.io/en/latest/index.html##
from anytree import Node, RenderTree

class Player(object):
    def __init__(self, name):
        self.name = name


    def generate_move(self, current_state):
        pass
            #minimax function

    def create_gametree(self, current_state: GameState, depth):
        starting_node = Node(current_state)
        for move in current_state.find_playable():
            new_state = current_state.set(move[0], move[1])
            Node(new_state, parent = starting_node)
        return starting_node

    def print_tree(start_node):
        for pre, fill, node in RenderTree(start_node):
            print("%s%s" % (pre, node.name))









