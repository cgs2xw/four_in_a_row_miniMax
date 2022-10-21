


class GameState(object):
    
    def __init__(self, state = None):
        #GameState attributes
        self.state = []     #board state
        self.moves = {}    #set with all moves played for x
        

        #if optional parameter not given, initiaize to empty
        if (not(isinstance(state, GameState))):
            for i in range(5):
                self.state.append([0] * 6)

        #if Gamestate object is passed to constructor
        else:
            for i in range(5):
                self.state.append(GameState[i])
            self.moves = GameState.moves
            



    #returns the value in the given position
    def get(self, x, y):
        
        return self.state[x][y]

    #sets a location on board to either an x or o
    #updates state as well as x and o move sets
    def set(self, x, y, value):
        
        if (value == 'x' or value == 'o'):
            self.xmoves.add((x,y, value))

        else:
            raise Exception("incorrect input must be x or o")
        self.state[y][x] = value

    #prints board
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

