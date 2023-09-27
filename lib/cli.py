# cli.py

from database import Players, Scene, Option, Prophecy, initialize_database, database

from helpers import *

# Initialize the database
initialize_database()

# Main menu loop
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Create Player")
        print("2. Delete Player")
        print("3. Display All Players")
        print("4. View Player's Choices")
        print("5. Find Player by Name")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_player()
        elif choice == "2":
            delete_player()
        elif choice == "3":
            display_all_players()
        elif choice == "4":
            view_player_choices()
        elif choice == "5":
            find_player_by_name()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()

if __name__ == "__main__":
    start_game()