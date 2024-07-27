import random
class WumpusGame:
    def __init__(self,size=4):
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.place_entities()
        self.agent_row = 0
        self.agent_col = 0
        self.play_game()
    def place_entities(self):
        self.place_entity(5, 'Breeze') #breeze
        self.place_entity(7,'Pit') #pit
        self.place_entity(9, 'Stench') #stench
        self.place_entity(6, 'Gold') #gold
        self.place_entity(-1, 'Wumpus') #Wumpus

    def place_entity(self, entity_code, entity_name):
        num_entities = random.randint(1,self.size)
        for _ in range(num_entities):
            row=random.randint(0,self.size - 1)
            col=random.randint(0,self.size - 1)
            while self.grid[row][col] != 0:
                row=random.randint(0,self.size - 1)
                col=random.randint(0,self.size - 1)
            self.grid[row][col] = entity_code
    def move_agent(self, new_row, new_col):
        if 0<=new_row<self.size and 0<=new_col<self.size:
            self.agent_row = new_row
            self.agent_col = new_col
            self.print_feedback()
        else:
            print('Invalid move!')
    def print_feedback(self):
        print("Now the agent is at{},{}".format(self.agent_row, self.agent_col))
        if self.grid[self.agent_row][self.agent_col]==5:
            print("You feel Breeze.")
        elif self.grid[self.agent_row][self.agent_col]==9:
            print("You smell Stench.")
        elif self.grid[self.agent_row][self.agent_col]==7:
            print("You fell into a pit.")
        elif self.grid[self.agent_row][self.agent_col]==6:
            print("You found Gold.")
        else:
            print("You are in an uneventful room.")
    def play_game(self):
        print("Initially agent is  at 0,0.")
        while True:
            print ("\nPossible Moves:")
            if self.agent_row+1<self.size:
                print("You can go at {} {}".format(self.agent_row+1, self.agent_col))
            if self.agent_col+1<self.size:
                print("You can go at {} {}".format(self.agent_row, self.agent_col+1))
            new_row=int(input("\nEnter input for row =>"))
            new_col=int(input("\nEnter input for column =>"))
            self.move_agent(new_row, new_col)
            if self.agent_row==0 and self.agent_col==0 and self.grid[0][0]==6:
                print("Congratulations! You won the game!")
                break
if __name__=="__main__":
    game= WumpusGame()

