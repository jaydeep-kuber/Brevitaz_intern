# ROCK PAPER SCISSORS
import random
import sys

print("Welcome in the ROCK PAPER SCISSORS game \n")

#global terms
wins = 0 
losses = 0
ties = 0

while True: # the main loop
    print("Current stats: \n wins:{0} \n losses:{1} \n ties: {2}".format(wins,losses,ties))
    while True: #player loop
        print("What is your move: (R:ROCK P:PAPER S:SCISSORS Q:QUIT)")
        player_move = input().lower()

        if player_move == 'q':
            print("Thanks for playing...")
            sys.exit() # Quit the program.

        if player_move == 'r' or player_move == 'p' or player_move == 's':
            print(f'You choose: {player_move}')
            break

    # Display what the computer chose:
    computer_move = random.choice(['r', 'p', 's'])
    print(f'Computer chose: {computer_move}')

    # winner conditions
    if player_move == computer_move:
        print('Tie!')
        print("--------------new game---------------")
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        print("--------------new game---------------")
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
         print('You win!')
         print("--------------new game---------------")
         wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
         print('You win!')
         print("--------------new game---------------")
         wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
         print('You lose!')
         print("--------------new game---------------")
         losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
         print('You lose!')
         print("--------------new game---------------")
         losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
         print('You lose!')
         print("--------------new game---------------")
         losses = losses + 1