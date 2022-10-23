from GameState import GameState
from Player    import Player



class Game(object):
    
    def __init__(self):
        self.currentState = GameState();
        self.player1 = Player("player1")
        self.player2 = Player("player2")



    def startGame(self):
        self.currentState.set(2,3,'x')
        self.currentState.set(2,2,'y')
        starting_node = self.player1.create_gametree(self.currentState, 2)
        self.player1.print_tree(starting_node)



