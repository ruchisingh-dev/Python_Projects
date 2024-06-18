import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 to {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    
    print(f"Bravo, you have guess the right number {random_number}")


def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too Low (L) or corrrect(C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"bravo Computer! You guesses it right. the number is {x}")


computerGuess(100)