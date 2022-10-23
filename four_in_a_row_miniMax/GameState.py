


class GameState(object):
    
    def __init__(self, state = None):
        #GameState attributes
        self.state = []     #board state
        self.moves = set()    #set with all moves played (x, y, value)

        #number in-a-rows for each type
        # pos 0 = x
        # pos 1 = o     
        self.twoOpen3 = [0,0]
        self.oneOpen3 = [0,0]
        self.twoOpen2 = [0,0]
        self.oneOpen2 = [0,0]

        self.eval = [0,0]
        self.moveNumber = 0

         

        #if optional parameter not given, initiaize to empty
        if (not(isinstance(state, GameState))):
            for i in range(5):
                self.state.append([0] * 6)

        #if Gamestate object is passed to constructor
        else:
            for i in range(5):
                self.state.append(GameState[i])
            self.moves = GameState.moves

            self.twoOpen3 = GameState.twoOpen3
            self.twoOpen2 = GameState.oneOpen2
            self.twoOpen2 = GameState.twoOpen2
            self.oneOpen2 = GameState.oneOpen2
            self.moveNumber = GameState.moveNumber



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
            if(x >= 0 and x < 6 and y >= 0 and y < 5):
                move = (x,y, value)
                if move not in self.moves:
                    self.moves.add(move)
                    self.state[y][x] = value
                    self.moveNumber += 1

                    if not (self.find_in_a_rows(x,y)):
                        self.calculate_eval()

                    else:
                        if (value == 'x'):
                            self.eval[0] = 1000
                            self.eval[1] = -1000
                        else:
                            self.eval[1] = 1000
                            self.eval[0] = -1000
                else:
                    raise Exception("move has already been played")
            else:
                raise Exception("x, y position out of range")
        else:
            raise Exception("incorrect input must be x or o")



    #prints board
    def print(self):
        for row in self.state:
            print(row)


    def printAll(self):
        self.print()
        print(f"move list  : {self.moves}\n")
        print(f"two open 3 : {self.twoOpen3}\n")
        print(f"one open 3 : {self.oneOpen3}\n")
        print(f"two open 2 : {self.twoOpen2}\n")
        print(f"one open 2 : {self.oneOpen2}\n")
        print(f"evaluation : {self.eval}\n")
        print(f"move number: {self.moveNumber}\n")



    #finds the number of 2 and 3 in a rows with correct openness, adds/subs gameState variables
    #takes in the most recent move, should be run in set function
    #returns true if 4 in a row is found false if not
    #does not fully calculate all in a rows if win is found
    #def find_in_a_rows(self, x, y):
    def find_in_a_rows(self, x, y):
        baseMoveType = self.get(x,y)
        middleTrack = set()

        for a in range(-1,2):                                               #offsets of -1 to 1 
            for b in range(-1,2):                                           #check all adjacent squares 
                if((x+a >= 0 and x+a < 6) and (y+b >= 0 and y+b < 5)):        #check if in board 
                    searchType = self.get(x+a, y+b)
                    #if not in middleTrack, to avoid double counting of x X x when searching left and right
                    if((x+a, y+b) not in middleTrack):
                        if(searchType != 0):                            #check if not empty

############################if the adjacent square is the same as middle###########################################################
                            if(searchType == baseMoveType):
                           
                                #if middle value is between too of is own kind (x X x)
                                if(self.get(x-a, y-b) == searchType):
                                    middleTrack.add((x-a,y-b))

                                    #four in a row either (x x X x) or (x X x x)
                                    if(self.get(a-(2*a), y-(2*b)) == searchType or self.get(a+(2*a), y+(2*b)) == searchType):
                                        return True

                                    #two open ( 0 x X x 0)
                                    elif(self.get(a-(2*a), y-(2*b)) == '0' and self.get(a+(2*a), y+(2*b)) == '0'):
                                        if(baseMoveType == 'x'): 
                                            self.twoOpen3[0] += 1
                                        else:
                                            self.twoOpen3[1] += 1

                                    #one open (0 x X x) or (x X x 0)
                                    elif(self.get(a-(2*a), y-(2*b)) == '0' or self.get(a+(2*a), y+(2*b)) == '0'):
                                        if(baseMoveType == 'x'): 
                                            self.oneOpen3[0] += 1
                                        else:
                                            self.oneOpen3[1] += 1


                                #four in a row (X x x x)
                                elif(self.get(x+(2*a), (y+(2*b))) == baseMoveType and self.get(x+(3*a), (y+(3*b))) == baseMoveType):
                                        return True

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

                                #if placed makes 0 open 3 (o x x X o)
                                else:
                                    if(baseMoveType == 'x'): 
                                        self.twoOpen2[0] += -1
                                    else:
                                        self.twoOpen2[1] += -1

                        
############################if the adjacent square the oposite of middle ( X o)###################################################
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
        return False



        
    #    #heuristic calculations
    def calculate_eval(self):
        self.eval[0] = 0
        self.eval[1] = 0
     
        for x in range(2):
            if (x == 0):
                y = 1
            else:
                y = 0

            self.eval[x] += (200*self.twoOpen3[x])
            self.eval[x] += (-80*self.twoOpen3[y])
            self.eval[x] += (150*self.oneOpen3[x])
            self.eval[x] += (-40*self.oneOpen3[y])
            self.eval[x] += (20*self.twoOpen2[x])
            self.eval[x] += (-15*self.twoOpen2[y])
            self.eval[x] += (5*self.oneOpen2[x])
            



 
    #def find_playable(self):
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
#def SW(type):
def SW(type):
    if(type == 'x'):
        type = 'o'
    elif(type == 'o'):
        type = 'o'
    return type