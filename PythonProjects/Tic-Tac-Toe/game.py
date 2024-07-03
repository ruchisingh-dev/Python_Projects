import time
from player import HumanPlayer, RandomCompPlayer, GeniusCompPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Use a single list to represent the 3x3 board
        self.currentWinner = None # Keep track of the winner

    def print_board(self):
        # Print the current board state
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Print the board with numbers (for user reference)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        # Return a list of available moves (indices of empty squares)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        # Check if there are any empty squares on the board
        return " " in self.board
    
    def num_empty_square(self):
        # Return the count of empty squares
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # Make a move if the square is valid and empty
        if self.board[square] == ' ':
            self.board[square] = letter 
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check if there is a winner after the move

        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check the diagonals (only if the move is on an even index)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
    
        # If no winning condition is met
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums() # Print the initial board numbers

    letter = 'X' # Starting letter

    while game.empty_square():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Make the move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to the square {square}")
                game.print_board()
                print('') # Empty line for readability
        
            if game.currentWinner:
                if print_game:
                    print(letter + " wins!")
                return letter
            # Alternate letters
            letter = 'O' if letter == 'X' else 'X'

        # Time pause for better visual experience
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    # o_player = RandomCompPlayer('O')
    o_player = GeniusCompPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
