


class GameState(object):
    
    def __init__(self, state = None):


        self.state = []
        self.movesMade = []

        if (not(isinstance(state, GameState))):
            for i in range(5):
                self.state.append([0] * 6)
        else:
            for i in range(5):
                self.state.append(GameState[i])



    def get(self, x, y):
        
        return self.state[x][y]

    def set(self, x, y, value):
        self.state[x][y] = value
        self.movesMade.append([x,y])

    def print(self):
        for row in self.state:
            print(row)



    #def detect_win(self, player):
    #def detect_tie(self):


    #def calculate_eval(self, player):
    #    #heuristic calculations

    #def detect_3rows(self, player):
    #def detect_2rows(self, player):

    def find_playable(self):
        avaliableMoves = [];
        for move in self.movesMade:
           for i in range(-1,2): 
                for j in range(-1,2):
                    if (move[0]+i) >= 0 and (move[0]+i) < len(self.state) and (move[1]+j) >= 0 and (move[1]+j) < len(self.state[0]) and self.get(move[0]+i,move[1]+j) != 'x' and self.get(move[0]+i,move[1]+j) != 'o':
                        if [move[0]+i,move[1]+j] not in avaliableMoves: #checking for duplicates not very efficent but works couldn't put the list in a set
                            avaliableMoves.append([move[0]+i,move[1]+j])
        return avaliableMoves

