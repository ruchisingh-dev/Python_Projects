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
    

# class GeniusCompPlayer(Player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         if len(game.available_moves()) == 9:
#             square = random.choice(game.available_moves())
#         else:
#             square = self.minimax(game, self.letter)['position']
#         return square

#     def minimax(self, state, player):
#         max_player = self.letter  # yourself
#         other_player = 'O' if player == 'X' else 'X'

#         # first we want to check if the previous move is a winner
#         if state.currentWinner == other_player:
#             return {'position': None, 'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (
#                         state.num_empty_square() + 1)}
#         elif not state.empty_square():
#             return {'position': None, 'score': 0}

#         if player == max_player:
#             best = {'position': None, 'score': -math.inf}  # each score should maximize
#         else:
#             best = {'position': None, 'score': math.inf}  # each score should minimize
#         for possible_move in state.available_moves():
#             state.make_move(possible_move, player)
#             sim_score = self.minimax(state, other_player)  # simulate a game after making that move

#             # undo move
#             state.board[possible_move] = ' '
#             state.current_winner = None
#             sim_score['position'] = possible_move  # this represents the move optimal next move

#             if player == max_player:  # X is max player
#                 if sim_score['score'] > best['score']:
#                     best = sim_score
#             else:
#                 if sim_score['score'] < best['score']:
#                     best = sim_score
#         return best

class GeniusCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in state.available_moves():
            # make a move, try that spot
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
