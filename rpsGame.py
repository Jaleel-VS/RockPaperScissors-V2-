import random, sys

print("ROCK, PAPER, SCISSORS")
# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:  # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)crssors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print("Type one of r, p, s, or q.")

    # Display what the player chose:
    rpsDict = {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}
    print(f"{rpsDict.get(playerMove)} versus...")

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    if randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    if randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")
    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose")
        losses += 1
