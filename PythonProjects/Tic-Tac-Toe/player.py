import math
import random 

class Player:
    def __init__(self, letter):
        # Initialize the player with a letter ('X' or 'O')
        self.letter = letter
    
    # Method to be overridden by subclasses to get their move in the game
    def get_move(self, game):
        pass

class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Choose a random valid move from available moves
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Loop until a valid move is entered
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                # Try to convert input to an integer
                val = int(square)
                # Check if the move is valid (square is available)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                # Print an error message for invalid input or unavailable move
                print('Invalid square. Try again.')
        return val
