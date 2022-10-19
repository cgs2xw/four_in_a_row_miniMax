


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
        
        return self.state[y][x]

    def set(self, x, y, value):
        self.state[y][x] = value



    def detect_win(self, player):
    def detect_tie(self):


    def calculate_eval(self, player):
    def detect_3rows(self, player):
    def detect_2rows(self, player):

    def find_playable(self):


