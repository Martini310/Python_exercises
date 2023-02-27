"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors,
    Scissors beats paper,
    Paper beats rock"""

rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


def winner(player1, player2):
    if player2 == rules[player1]:
        return "Player 1 wins!"
    elif player1 == player2:
        return "Draw!"
    else:
        return "Player 2 wins!"


while True:
    p1 = input("Player 1 (rock, paper, scissors): ")
    if p1 not in rules.keys():
        print("Chose from given scope: rock, paper, scissors.")
        continue
    p2 = input("Player 2 (rock, paper, scissors): ")
    if p2 not in rules.keys():
        print("Chose from given scope: rock, paper, scissors.")
        continue
    print(winner(p1, p2))
    p = input("Play again? (y/n): ")
    if p == 'n':
        print("Thank you for the game!")
        break
