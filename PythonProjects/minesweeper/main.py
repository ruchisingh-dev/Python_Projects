import random


# lets create a board object to represent the monesweeper game
# this is so that we can just say "create a new board object"
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, no_bomb):
        # let's keep track of these parameter. they'll be helpfull later
        self.dim_size = dim_size
        self.no_bombs = no_bomb

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
        while bombs_planted < self.num_bombs:
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


# play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bomb
    # step 2: show user the box and ask for where they want to dig
    # step 3a: if location is a bomb, show game over massage
    # step 3b: id location is not bomb, dig recursively until each square is at least next to bomb
    # step 4: repeat step 2 and 3a/b until there are no more places to dig
    pass