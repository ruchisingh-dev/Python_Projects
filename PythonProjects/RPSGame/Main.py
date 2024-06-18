import random 

def play():
    user = input("'r' for rock, 'p' for paper and 's; for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'
    
    if is_win(user, computer):
        return f'you won! computer chooses {computer}'
    
    return f"you lose! computer chooses {computer}"
    
    

def is_win(player, component):
    # returns player wins if it is true
    # r>s, s>p, p>r
    if (player == 'r' and component == 's') or (player == 's' and component == 'p') or (player == 'p' and component == 'r'):
        return True
    

print(play())