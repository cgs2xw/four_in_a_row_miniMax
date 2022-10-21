


class GameState(object):
    
    def __init__(self, state = None):


        self.state = []

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
        for x in range(len(self.state)):
            for y in range(len(self.state[0])):
                if self.get(x,y) == 'x' or self.get(x,y) == 'o':
                    for i in range(-1,2): 
                        for j in range(-1,2):
                            if (x+i) >= 0 and (x+i) < len(self.state) and (y+j) >= 0 and (y+j) < len(self.state[0]) and self.get(x+i,y+j) != 'x' and self.get(x+i,y+j) != 'o':
                                if [x+i,y+j] not in avaliableMoves: #checking for duplicates not very efficent but works couldn't put the list in a set
                                    avaliableMoves.append([x+i,y+j])
        return avaliableMoves

