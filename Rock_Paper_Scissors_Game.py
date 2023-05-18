import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nChoose rock/paper/scissors. Press S to stop playing. ")
    if user_input == "s":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You picked rock... you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You picked paper... you won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You picked scissors... you won!")
        user_wins += 1

    else:
        print("The computer won!")
        computer_wins += 1

print("\nUser score:", user_wins)
print("Computer score:", computer_wins)
print("Thanks for playing, goodbye! :)")

