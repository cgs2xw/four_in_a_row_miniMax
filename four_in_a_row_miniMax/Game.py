from GameState import GameState
from Player    import Player
import time



class Game(object):
    
    def __init__(self):
        self.currentState = GameState();
        self.player1 = Player("player1")
        self.player2 = Player("player2")



    def startGame(self):
        self.currentState.set(2,3,'x')
        self.currentState.set(2,2,'o')
        
        #self.currentState.set(1,2,'x')
        #self.currentState = self.player1.generate_move(self.currentState, 'o', 4)
        #self.currentState.printAll()
        i = 0
        while(not (self.currentState.win or self.currentState.draw)):
            start_time = time.time()
            if i % 2 == 0:
                self.currentState = self.player1.generate_move(self.currentState, 'x', 2)
            else:
                self.currentState = self.player2.generate_move(self.currentState, 'o', 4)
            i += 1
            self.currentState.printAll()
            
            print("%s seconds for move" % (time.time() - start_time))
        




