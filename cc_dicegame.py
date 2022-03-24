import random

high_score = 0
dice_roll1 = random.randint(1, 6)
dice_roll2 = random.randint(1, 6)

def dice_game():
    while True:
        global high_score
        print("Current high score: ", high_score)
        print("(1) Roll Dice")
        print("(2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou rolled a...", dice_roll1)
            print("You rolled a...", dice_roll2)
            print("\nYou have rolled a total of:", dice_roll1 + dice_roll2)
            high_score = dice_roll1 + dice_roll2
            if dice_roll1 + dice_roll2 > high_score:
                print("\nNew high score!")
        elif choice == "2": 
            print("Goodbye!")
            break
        else:
            print("Unknown choice")

dice_game()