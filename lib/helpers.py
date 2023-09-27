# helpers.py

from database import *

# Create a player
def create_player():
    name = input("Enter player name: ")

    player = Players.create(player_name=name)
    print(f"Player {player.player_name} created successfully.")

# Delete a player
def delete_player():
    player_id = int(input("Enter player ID: "))

    try:
        player = Players.get(Players.player_id == player_id)
        player.delete_instance()
        print(f"Player {player.player_name} deleted successfully.")
    except Players.DoesNotExist:
        print("Player not found.")

# Display all players
def display_all_players():
    players = Players.select()

    if players:
        for player in players:
            print(f"ID: {player.player_id}, Name: {player.player_name}, Scene ID: {player.scene_id}")
    else:
        print("No players found.")

# View player's choices
def view_player_choices():
    player_id = int(input("Enter player ID: "))

    try:
        player = Players.get(Players.id == player_id)
        choices = player.choices

        if choices:
            for choice in choices:
                print(f"Choice: {choice.text}, Outcome: {choice.outcome}")
        else:
            print("No choices found for this player.")
    except Players.DoesNotExist:
        print("Player not found.")

# Find player by name
def find_player_by_name():
    name = input("Enter player name: ")

    players = Players.select().where(Players.name == name)

    if players:
        for player in players:
            print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}")
    else:
        print("Player not found.")

