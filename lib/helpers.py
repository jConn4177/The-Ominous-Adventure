# helpers.py


# Create a player
def create_player():
    name = input("Enter player name: ")

    player = Players.create(name=name)
    print(f"Player {player.name} created successfully.")

# Delete a player
def delete_player():
    player_id = int(input("Enter player ID: "))

    try:
        player = Player.get(Player.id == player_id)
        player.delete_instance()
        print(f"Player {player.name} deleted successfully.")
    except Player.DoesNotExist:
        print("Player not found.")

# Display all players
def display_all_players():
    players = Player.select()

    if players:
        for player in players:
            print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}")
    else:
        print("No players found.")

# View player's choices
def view_player_choices():
    player_id = int(input("Enter player ID: "))

    try:
        player = Player.get(Player.id == player_id)
        choices = player.choices

        if choices:
            for choice in choices:
                print(f"Choice: {choice.text}, Outcome: {choice.outcome}")
        else:
            print("No choices found for this player.")
    except Player.DoesNotExist:
        print("Player not found.")

# Find player by name
def find_player_by_name():
    name = input("Enter player name: ")

    players = Player.select().where(Player.name == name)

    if players:
        for player in players:
            print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}")
    else:
        print("Player not found.")

