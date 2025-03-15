

def guess_number_game():
    import random
    number_to_guess = random.randint(1, 25)
    attempts = 0
     
    print("⊱ ──────── {⋆ Welcome to the Guess the Number game!⋆} ────────── ⊰ ")
    print("Guess what I am thinking.\nI'm thinking of a number between 1 and 25.\n★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! ❌ Try again.")
        elif guess > number_to_guess:
            print("Too high! ❌ Try again.")
        else:
            print(f"Congratulations 😜 ! You guessed the number in {attempts} attempts.")
            print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
            break

def rock_paper_scissors_game():
    import random

    game_choices = ["rock", "paper", "scissors"]
    computer = random.choice(game_choices)

    print("⊱ ──────── {⋆ Welcome to Rock-Paper-Scissors!(✌️  ✊ ✋) ⋆} ────────── ⊰")
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")

    if player not in game_choices:
        print("Invalid choice ❌. Please enter rock, paper, or scissors.")
        return

    print("Computer has chosen: ",computer,"!!!")

    if player == computer:
        print("It's a tie(-_-)!\n Come again next time")
    elif (player == "rock" and computer == "scissors"):
        print("You win ❣ Congratulations ♡ \nCome win again next time")
    elif (player == "paper" and computer == "rock"):
        print("You win ❣ Congratulations ♡\nCome win again next time")
    elif (player == "scissors" and computer == "paper"):
        print("You win ❣ Congratulations ♡\nCome win next time")
    else:
        print("You lose ❌! Better luck next time ☹ \nCome again and win next time ")


def main_menu():
    while True:
        print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
        print("Select a game (1-3):")
        print("1. Guess the Number game 🤔 ")
        print("2. Rock-Paper-Scissors game(✌️  ✊ ✋)")
        print("3. Exit program")
        print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")

        choice = input("Enter your choice: ")

        if choice == '1':
            guess_number_game()
            
        elif choice == '2':
            rock_paper_scissors_game()

        elif choice == '3':
            print("Exiting program. Goodbye!")
            print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")

        if choice != '3':
            again = input("Would you like to play another game? (y/n): ").lower()
            print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
            if again != 'y':
                print("Exiting program. Goodbye!")
                print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
                break


main_menu()