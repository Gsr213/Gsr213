from ast import And


class tictactoe():
    spaces = [[' ','A','B','C'],['1',' ',' ',' '],['2',' ',' ',' '],['3',' ',' ',' ']]

    def show_board(self):
        print("Showing Game Board!")
        for s in self.spaces:
            print(s[0] + "|" + s[1] + "|" + s[2] + "|" + s[3] + "|")
        print("\n")

    def game_loop(self):
        turns = 0
        while(turns < 8):
            self.show_board()
            first_move = input("Player 1 enter a space! Please enter column and then row (Ex. A1): ")
            self.play_space('X',first_move)
            self.show_board()
            if self.check_winner():
                print("Player 1 wins!")
                return
            turns += 1
            second_move = input("Player 2 enter a space! Please enter column and then row (Ex. A1): ")
            self.play_space('O',second_move)
            self.show_board()
            if self.check_winner():
                print("Player 2 wins!")
                return
            turns += 1
        print("Draw!")
        return

    def check_winner(self):
        #Check for the 8 potential winning patterns:
        #1: Vertical first column
        if self.spaces[1][1] == self.spaces[2][1] == self.spaces[3][1]:
            if (self.spaces[1][1] != ' ') and (self.spaces[2][1] != ' ') and (self.spaces[3][1] != ' '):
                return True
            else:
                return False
        #2: Vertical second column
        elif self.spaces[1][2] == self.spaces[2][2] == self.spaces[3][2]:
            if (self.spaces[1][2] != ' ') and (self.spaces[2][2] != ' ') and (self.spaces[3][2] != ' '):
                return True
            else:
                return False
        #3: Vertical third column
        elif self.spaces[1][3] == self.spaces[2][3] == self.spaces[3][3]:
            if (self.spaces[1][3] != ' ') and (self.spaces[2][3] != ' ') and (self.spaces[3][3] != ' '):
                return True
            else:
                return False
        #4: Horizontal first row
        elif self.spaces[1][1] == self.spaces[1][2] == self.spaces[1][3]:
            if (self.spaces[1][1] != ' ') and (self.spaces[1][2] != ' ') and (self.spaces[1][3] != ' '):
                return True
            else:
                return False
        #5: Horizontal second row
        elif self.spaces[2][1] == self.spaces[2][2] == self.spaces[2][3]:
            if (self.spaces[2][1] != ' ') and (self.spaces[2][2] != ' ') and (self.spaces[2][3] != ' '):
                return True
            else:
                return False
        #6: Horizontal third row
        elif self.spaces[3][1] == self.spaces[3][2] == self.spaces[3][3]:
            if (self.spaces[3][1] != ' ') and (self.spaces[3][2] != ' ') and (self.spaces[3][3] != ' '):
                return True
            else:
                return False
        #7: Diagonal upper left to lower right
        elif self.spaces[1][1] == self.spaces[2][2] == self.spaces[3][3]:
            if (self.spaces[1][1] != ' ') and (self.spaces[2][2] != ' ') and (self.spaces[3][3] != ' '):
                return True
            else:
                return False
        #8: Diagonal upper right to lower left
        elif self.spaces[1][3] == self.spaces[2][2] == self.spaces[3][1]:
            if (self.spaces[1][3] != ' ') and (self.spaces[2][2] != ' ') and (self.spaces[3][1] != ' '):
                return True
            else:
                return False
        else:
            return False

    def play_space(self, mark, space):
        col = 0
        if space[0] == 'A' or space[0] == 'B' or space[0] == 'C':
            if space[0] == 'A':
                col = 1
            if space[0] == 'B':
                col = 2
            if space[0] == 'C':
                col = 3
            if space[1] == '1' or space[1] == '2' or space[1] == '3':
                self.spaces[int(space[1])][col] = mark
            else:
                print("Invalid space! Please re-enter.")
        else:
            print("Invalid space! Please re-enter.")
            
        
        

print("Welcome to TicTacToe!")
print("A game between two opponents, fighting to make a sequence of three for their mark which is either X or O!\n")

print("Player 1 goes first and uses the 'X' mark!")
print("Player 2 goes second and uses the 'O' mark!\n")

t = tictactoe()
t.game_loop()