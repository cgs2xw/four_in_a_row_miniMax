


class GameState(object):
    
    def __init__(self, state = None):
        #GameState attributes
        self.state = []     #board state
        self.moves = {}    #set with all moves played for x

        #number in-a-rows for each type
        # pos 0 = x
        # pos 1 = o     
        self.twoOpen3 = [0,0]
        self.oneOpen3 = [0,0]
        self.twoOpen2 = [0,0]
        self.oneOpen2 = [0,0]

        self.eval = [0,0]


        

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
        
        if(x > 0 and x < 6 and y > 0 and y < 5):
            return self.state[y][x]
        else:
            return 'w'          # W for wall e.g. edge of board/outside board. really only need to be differnt than x o and 0

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



    def detect_win(self, player):
        pass
    def detect_tie(self):
        pass

    #finds the number of 2 and 3 in a rows with correct openness, adds/subs gameState variables
    #takes in the most recent move, should be run in set function
    def find_in_a_rows(self, x, y):
        baseMoveType = self.get(x,y)


        for a in range(-1,2):                                               #offsets of -1 to 1 
            for b in range(-1,2):                                           #check all adjacent squares 
                if((x+a > 0 and x+a < 6) and (y+b > 0 and y+b < 5)):        #check if in board 
                    searchType = self.get(x+a, y+b)

                    if(searchType != 0):                            #check if not empty

                        #if the adjacent square is the same as middle
                        if(searchType == baseMoveType):
                           
                            #if middle value is between too of is own kind x X x ########################################################
                            #needs to be implimented
                            if(self.get(x-a, y-b) == searchType):
                                pass


                            #if two away is the same as base value (X x x)
                            elif(self.get(x+(2*a), (y+(2*b))) == baseMoveType):
                                if(self.get(x+(3*a), (y+(3*b))) == baseMoveType):
                                    if(baseMoveType == 'x'):
                                        self.eval[0] = 1000
                                        self.eval[1] = -1000
                                    else:
                                        self.eval[1] = 1000
                                        self.eval[0] = -1000
                                    return


                            #if two sides open (0 X x x 0)
                            elif(self.get(x+(2*a), (y+(2*b))) == 0 and self.get(x-a, y-b) == 0):
                                if(baseMoveType == 'x'): 
                                    self.twoOpen2[0] += 1
                                else:
                                    self.twoOpen2[1] += 1

                            #if one side open (X x x 0)
                            elif(self.get(x+(2*a), (y+(2*b))) == 0 or self.get(x-a, y-b) == 0):
                                if(baseMoveType == 'x'): 
                                    self.twoOpen2[0] += 1
                                else:
                                    self.twoOpen2[1] += 1

                        
                        #if the adjacent square the oposite of middle ( X o)
                        else:
                            #if three in a row  of other type next to start position (X o o o)
                            if(self.get(x+a, y+b) == SW(baseMoveType) and self.get(x+(2*a), (y+(2*b))) == SW(baseMoveType) and self.get(x+(3*a), (y+(3*b)) == SW(baseMoveType))):
                                if(self.get(x+(4*a), (y+(4*b))) == 0):
                                    if(baseMoveType == 'x'):
                                        self.twoOpen3[1] += -1
                                        self.oneOpen3[1] += 1
                                    else:
                                       self.twoOpen3[0] += -1
                                       self.oneOpen3[0] += 1
                                        
                                else:
                                    if(baseMoveType == 'x'):
                                        self.oneOpen3[1] += -1
                                    else:
                                        self.oneOpen3[0] += -1

                            #if two in a row of other type next to start position(X o o)
                            elif((self.get(x+a, y+b) == SW(baseMoveType) and self.get(x+(2*a), (y+(2*b))) == SW(baseMoveType))):
                                if(self.get(x+(3*a), (y+(3*b))) == 0):
                                    if(baseMoveType == 'x'):
                                        self.twoOpen2[1] += -1
                                        self.oneOpen2[1] += 1
                                    else:
                                       self.twoOpen2[0] += -1
                                       self.oneOpen2[0] += 1

                                else:
                                    if(baseMoveType == 'x'):
                                        self.oneOpen2[1] += -1
                                    else:
                                        self.oneOpen2[0] += -1



        
    #    #heuristic calculations
    def calculate_eval(self):
        pass

 
    
    def find_playable(self):
        avaliableMoves = [];
        for move in self.movesMade:
           for i in range(-1,2): 
                for j in range(-1,2):
                    if (move[0]+i) >= 0 and (move[0]+i) < len(self.state) and (move[1]+j) >= 0 and (move[1]+j) < len(self.state[0]) and self.get(move[0]+i,move[1]+j) != 'x' and self.get(move[0]+i,move[1]+j) != 'o':
                        if [move[0]+i,move[1]+j] not in avaliableMoves: #checking for duplicates not very efficent but works couldn't put the list in a set
                            avaliableMoves.append([move[0]+i,move[1]+j])
        return avaliableMoves


#returns oposite of 
def SW(type):
    if(type == 'x'):
        type = 'o'
    elif(type == 'o'):
        type = 'o'
    return type