import random
import re


# lets create a board object to represent the monesweeper game
# this is so that we can just say "create a new board object"
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, no_bomb):
        # let's keep track of these parameter. they'll be helpfull later
        self.dim_size = dim_size
        self.no_bomb = no_bomb

        # lets's create the board
        # helper function
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which location we've uncovered
        # we'll have (row, col) tuple into this set
        self.dug = set() # if we dug at 0,0 the self.dug = {(0,0)}


    def make_new_board(self):
        # construct a new board on the dim size and num bombs
        # we should construct the list of lists here(becoz we have 2D board)

        # generate the board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this create a array like this 
        # [[ None, None,.......None,
        # None, None,.......None,
        # None, None,.......None,
        # None, None,.......None,
        # None, None,.......None]]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.no_bomb:
            loc = random.randint(0, self.dim_size**2 -1) # return a integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_s9ze goes into loc to tell us what row to look at
            col = loc % self.dim_size # we want the remainder to tell us what index in that row to look at
            if board[row][col] == '*':
                # this mean we've actually planted the boam there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    # if this already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        num_neighboring_bombs = 0
        for r in range (max(0, row-1), min(self.dim_size-1,row+1)+1):
            for c in range (max(0,col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs+=1
        return num_neighboring_bombs


    def dig(self, row, col):
        # dig at the location
        # return true if successful dig, false if bomb dug
        

        # few scenerio
        # hit a bomb --> game over
        # dig at location with neiboring bombs --> finish dig
        # dig at the location with no neiboring bomb --> recursively dig neighbors
        self.dug.add((row, col)) # keep track the we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        # self.board[row][col] == 0
        for r in range (max(0, row-1), min(self.dim_size-1,row+1)+1):
            for c in range (max(0,col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue # don't dig where you already dug
                self.dig(r, c)
        
        # if our initial dug didn't hit the a bomb, then we shouldn't hit the bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep



# play the game
def play(dim_size=10, no_bomb=10):
    # step 1: create the board and plant the bomb
    board = Board(dim_size, no_bomb)
    # step 2: show user the box and ask for where they want to dig
    # step 3a: if location is a bomb, show game over massage
    # step 3b: id location is not bomb, dig recursively until each square is at least next to bomb
    # step 4: repeat step 2 and 3a/b until there are no more places to dig
    safe = True

    while len(board.dug) < board.dim_size ** 2 - no_bomb:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try Again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # you dug a bomb 
            break

    # 2 ways to end loop, let's check which one
    if safe:
        print("CONGRACTULATION!!! YOU ARE VICTORIOUS")
    else:
        print("SORRY GAME OVER")
        # Let's reveal the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': 
    play()