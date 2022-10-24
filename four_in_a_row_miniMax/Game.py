from GameState import GameState
from Player    import Player



class Game(object):
    
    def __init__(self):
        self.currentState = GameState();
        self.player1 = Player("player1")
        self.player2 = Player("player2")



    def startGame(self):
        self.currentState.set(2,3,'x')
        self.currentState.set(2,2,'o')
        
       
        i = 0
        while(not (self.currentState.win and self.currentState.draw)):
            if i % 2 == 0:
                self.currentState = self.player1.generate_move(self.currentState, 'x', 2)
            else:
                self.curentState = self.player2.generate_move(self.currentState, 'o', 4)
            i += 1
            self.currentState.printAll()
        




