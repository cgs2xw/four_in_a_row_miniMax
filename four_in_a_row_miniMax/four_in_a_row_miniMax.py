from GameState import GameState



if __name__ == "__main__":
    mystate = GameState()
    mystate.set(2,3,'x')
    mystate.set(2,2,'y')
    
   

    print(mystate.state)
