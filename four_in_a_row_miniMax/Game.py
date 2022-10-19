from GameState import GameState
from Player    import Player



class Game(object):
    
    def __init__(self):
        currentState = GameState();
        player1 = Player("player1")
        player2 = Player("player2")



    def startGame(self):
        self.currentState.set(2,3,'x')
        self.currentState.set(2,2,'y')
        while():#game is not over
            gameOptions = self.GameState.find_playable



