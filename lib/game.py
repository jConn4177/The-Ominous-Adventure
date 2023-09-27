# game.py

from cli import main_menu
from database import BaseModel, Players, Scene, Option, Prophecy

def start_game():
    print("Welcome to 'The Ominous Encounter'!")

    # Create a new player
    player_name = input("Enter your name: ")

    player = Players.create(name=player_name)

    print(f"Hello, {player.player_name}! Let's begin the adventure.")

    # Start the game loop
    while True:
        print("\n---")
        print("Options:")
        print("1. Join your friends for more shots")
        print("2. Opt for a more mellow approach, sipping on lemonade")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            more_shots(player)
        elif choice == "2":
            sip_lemonade(player)
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def more_shots(player):
    print("You choose to have more shots with your friends.")
    print("The night spirals into a blur of fun and laughter.")

    # Implement the game over scenario
    print("However, as the night progresses, so does the intoxication.")
    print("You’ve gone too far and have to taxi home before midnight.")
    print("Game over.")

def sip_lemonade(player):
    print("You sip on lemonade, savoring the refreshing taste as you engage in delightful conversations with your friends.")
    print("At one point, you decide to step outside for a quick vape break.")

    # Implement the next part of the game
    print("As you exhale a puff of vapor, you notice a black cat with striking green eyes in the yard, peacefully minding its own business.")

    while True:
        print("\n---")
        print("Options:")
        print("1. Continue vaping and head back inside")
        print("2. Curiosity gets the better of you, and you decide to follow the cat behind the shed")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You continue vaping and head back inside, rejoining the festivities.")
            print("Game over.")
            break
        elif choice == "2":
            follow_cat(player)
            break
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def follow_cat(player):
    print("You stealthily follow the mysterious feline behind the shed, only to find that it has vanished without a trace.")
    print("Instead, you encounter something utterly unexpected—a colossal pile of black ooze.")
    print("It ripples and shifts, and from the center emerges a massive bright blue eye, akin to the evil eye shade of blue with a black center.")
    print("The eye locks onto you, its presence unnerving.")

    while True:
        print("\n---")
        print("Options:")
        print("1. Press enter to continue")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            encounter_ooze(player)
            break
        elif choice == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def encounter_ooze(player):
    print("The tone shifts from the jovial party atmosphere to an eerie, all-knowing aura.")
    print("The ooze speaks to you through telepathy, its voice echoing in your mind.")

    while True:
        print("\n---")
        print("Options:")
        print("1. Attempt to run from the ooze")
        print("2. Share something unrelated")
        print("3. Express your desire for a prophecy")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You make a frantic attempt to escape, but the ooze moves with incredible speed, enveloping you and absorbing you into its collective consciousness for all eternity.")
            print("Game over.")
            break
        elif choice == "2":
            print("You decide to play along and share something unrelated.")
            print("The ooze remains silent, uninterested in your words.")
        elif choice == "3":
            print("You express your desire for a prophecy.")
            print("The ooze's massive blue eye flickers with amusement, and it imparts its wisdom.")
            print("THE END")
            print("The eye's gaze intensifies, and before you can react, it knocks you out.")
            print("When you wake up, you find yourself on the porch, a prophecy etched onto the inside of your arm, your mind forever marked by the encounter.")
            print("(Prophecy)")
            print("Game over.")
            break
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    start_game()