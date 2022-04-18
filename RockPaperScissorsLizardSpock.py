import random

user_score = 0
computer_score = 0
end_score = 4 # best of 7 games
game_choices = {'1': 'rock', '2': 'paper', '3': 'scissors', '4': 'lizard', '5': 'spock'}

print("\nWinning Rules of Rock Paper Scissors Lizard Spock: \n"
        "\n"
        "Scissors cuts Paper \n"
        "Paper covers Rock \n" 
        "Rock crushes Lizard \n"
        "Lizard poisons Spock \n"
        "Spock smashes Scissors \n"
        "Scissors decapitates Lizard \n"
        "Lizard eats Paper \n"
        "Paper disproves Spock \n"
        "Spock vaporizes Rock \n"
        "(and as it always has) Rock crushes Scissors \n")

print("Best of 7 games!\n")
while True:
    user_choice = input("\n1) Rock, 2) paper, 3) scissors, 4) lizard, or 5) Spock? Input 1-5: ")
    comp_choice = random.choice(["1", "2", "3", "4", "5"])
    print("\nYou chose " + game_choices[user_choice])
    print("Computer chose " + game_choices[comp_choice] + "\n")
    if user_choice == comp_choice:
        print("It's a tie!")
    elif user_choice == "1":
        if comp_choice == "3":
            print("Rock crushes Scissors. You win!\n")
            user_score += 1
        elif comp_choice == "4":
            print("Rock crushes Lizard. You win!\n")
            user_score += 1
        else:
            print("You lose! Try again!\n")
            computer_score += 1
    elif user_choice == "2":
        if comp_choice == "1":
            print("Paper covers Rock. You win!\n")
            user_score += 1
        elif comp_choice == "5":
            print("Paper disproves Spock. You win!\n")
            user_score += 1
        else:
            print("You lose! Try again!\n")
            computer_score += 1
    elif user_choice == "3":
        if comp_choice == "2":
            print("Scissors cuts Paper. You win!\n")
            user_score += 1
        elif comp_choice == "4":
            print("Scissors decapitates Lizard. You win!\n")
            user_score += 1
        else:
            print("You lose! Try again!\n")
            computer_score += 1
    elif user_choice == "4":
        if comp_choice == "2":
            print("Lizard eats Paper. You win!\n")
            user_score += 1
        elif comp_choice == "5":
            print("Lizard poisons Spock. You win!\n")
            user_score += 1
        else:
            print("You lose! Try again!\n")
            computer_score += 1
    elif user_choice == "5":
        if comp_choice == "1":
            print("Spock smashes Scissors. You win!\n")
            user_score += 1
        elif comp_choice == "3":
            print("Spock vaporizes Rock. You win!\n")
            user_score += 1
        else:
            print("You lose! Try again!\n")
            computer_score += 1
    else:
        print("Invalid input. Try again!\n")
        continue
    print("Your score: ", user_score)
    print("Computer score: ", computer_score)
    if user_score == end_score or computer_score == end_score:
        if user_score > computer_score:
            print("You win this round!")
        elif user_score < computer_score:
            print("You lose this round!")
        else:
            print("It's a tie!")
        play_again = input("Play again? (y/n): ")
        if play_again == "n":
            print("Thanks for playing! Goodbye!")
            break
        elif play_again == "y":
            user_score = 0
            computer_score = 0
            continue
        else:
            print("Invalid input. Try again!")
            continue





