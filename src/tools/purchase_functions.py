from src.base_classes.player import player
from src.Tools.json_handler import update_json, read_json
from src.common_variables import *
from src.base_classes.game_state import game
import pygame

# Closing function for yes-no choice screens (e.g. purchase & equip)
def close_yes_no(class_name, visibility):
    setattr(class_name, visibility, False)

def equipping_or_purchase(selected_item, screen, image_type, position):
    # Determining which flag to draw
    if image_type == "purchase":
        image_path = "images/Game_Shop/Purchased.png"
    elif image_type == "equipped":
        image_path = "images/Game_Shop/Equipped.png"

    # Getting the coordinates of the selected item
    # and positioning the flag relative to it
    item_rect = selected_item.get_rect()
    width = item_rect.width
    height = item_rect.height
    x_pos = position[0]
    y_pos = position[1]

    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))

    screen.blit(image, (x_pos, y_pos))

# Copying the old values from the player class and recreating
# them with updated attributes for the most recent purchase.
def recreate_players(new_health=None):
    old_values = \
        {"Weapon": game.player1.current_weapon,
        "Position Player 1": game.player1.position,
        "Position Player 2": game.player2.position if game.player2 else None, # Format to only access player 2 attributes when they exist
        "Health Player 1": game.player1.health,
        "Health Player 2": game.player2.health if game.player2 else None,
        "Coin Balance": game.player1.coin_balance,
        "Old Weapon": game.player1.current_weapon,
        "Player 1 Number": game.player1.player_number,
        "Player 2 Number": game.player2.player_number if game.player2 else None,
        }

    # Emptying the sprite group so that the old players are deleted.
    game.player_sprite_group.empty()

    # Creating new versions of each player if they exist
    if game.player1:
        game.player1 = player(old_values["Weapon"])
        game.player1.position = old_values["Position Player 1"]
        game.player1.health = new_health if new_health else old_values["Health Player 1"]
        game.player1.coin_balance = old_values["Coin Balance"]
        game.player1.current_weapon = old_values["Old Weapon"]
        game.player1.player_number = old_values["Player 1 Number"]
        game.player_sprite_group.add(game.player1)

    if game.player2 == None:
        print("No second player")
    else:
        game.player2 = player(old_values["Weapon"])
        game.player2.position = old_values["Position Player 2"]
        game.player2.health = new_health if new_health else old_values["Health Player 1"]
        game.player2.coin_balance = old_values["Coin Balance"]
        game.player2.current_weapon = old_values["Old Weapon"]
        game.player2.player_number = old_values["Player 2 Number"]
        game.player_sprite_group.add(game.player2)

# Closing the purchase menu if the user presses the no button
def no(class_name):
    close_yes_no(class_name, "purchase_background_visibility")

def purchase(price, name, players_list, instance_name, class_name):
    # Ensuring the players have been initialized before allowing them to purchase an item.
    if game.player_button_clicked_state:
        # Ensuring the players have enough money to buy the item
        # and subtracting the price from their game balance.
        if all(p.coin_balance >= price for p in players_list):
            for p in players_list:
                p.coin_balance -= price

            print(f"{name.title()} was bought from the item shop. New Player Balance: {p.coin_balance}\n")

            instance_name.item_purchased = True

        # Todo: replace with not enough money image
        # else:
        #     message = "Not enough money to purchase this item"
        #     font = pygame.font.SysFont('Courier New', 15, True, False)
        #     text = font.render(message, True, WHITE)
        #     purchase_surface.blit(text, (30, 30))

        # Closing the purchase screen after the transaction is complete.
        close_yes_no(class_name, "purchase_background_visibility")

# Equipping function actually equips the item and prevents double purchasing
def equip(obj, close, item_type, item_info, image_path,
          name, players_list):
    setattr(obj, "equipped", True)

    for p in players_list:
    # If a ship item is purchased, health, velocity and sprite image are updated.
        if item_type == "ships":
            p.health = item_info.get("Health")
            new_movement_speed = item_info.get("Velocity")
            new_player_sprite_path = image_path
            print(new_player_sprite_path)
            update_json("players", {"Movement_Speed" : new_movement_speed})
            update_json("players", {"Sprite" : new_player_sprite_path})
            recreate_players() # After each purchase, the players are recreated to display changes in real time.

        # If a weapon is purchased, the type of bullet shot is changed. So is the damage and speed.
        elif item_type == "weapons":
            current_weapon = p.current_weapon
            print(f"Current weapon: {current_weapon}")
            p.current_weapon = name
            new_weapon = p.current_weapon
            print("blasters running")
            recreate_players()
            print(f"New Weapon = {new_weapon}")


        # Updating player attributes when an upgrade is bought.
        if item_type == "upgrades":
            # Damage increases
            weapon_name = p.current_weapon
            damage = p.all_weapons[weapon_name]["Damage"]
            print(weapon_name)
            print(f"Current damage: {damage}")
            damage_increase = item_info.get("Increase Damage", 0)  # Defaulting to 0 if no value is provided.
            new_damage = damage + damage_increase
            update_json("weapons", {f"{weapon_name}.Damage" : new_damage})
            print(f"New damage: {new_damage}")

            # Health increases
            print(f"Current health: {p.health}")
            p.health += item_info.get("Increase Health", 0)
            print(f"New health: {p.health}\n")

            # Movement speed increases
            Movement_Speed = p.MOVEMENT_SPEED
            print(f"Current Movement Speed: {Movement_Speed}")
            movement_increase = item_info.get("Movement Speed Increase", 0)
            new_movement_speed = Movement_Speed + movement_increase
            update_json("players", {"Movement_Speed" : new_movement_speed})
            updated_movement_speed = read_json("players", ["Movement_Speed"])
            print(f"New Movement Speed: {updated_movement_speed}")
            recreate_players()

# If the player does not have enough money, a notice is returned and the equipping is closed.
    close()