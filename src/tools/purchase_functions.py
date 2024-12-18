from src.base_classes.game_state import game
from src.base_classes.player import player
from src.Tools.json_handler import update_json, read_json
from src.common_variables import *
from src.base_classes.game_state import game
import pygame

def draw_choice_buttons(class_name, button_yes, button_no):
    yes_button = getattr(class_name, button_yes)
    no_button = getattr(class_name, button_no)
    yes_button.draw()
    no_button.draw()

def close_purchase(class_name, visibility):
    setattr(class_name, visibility, False)

def equipping(selected_item, screen):
    print("running equipping function")
    item_rect = selected_item.get_rect()
    width = item_rect.width
    height = item_rect.height
    x_pos = item_rect.x
    y_pos = item_rect.y

    equipped_image = pygame.image.load("images/Game_Shop/Equipped.png")
    equipped_image = pygame.transform.scale(equipped_image, (width, height))

    screen.blit(equipped_image, (x_pos, y_pos))

def recreate_players(new_weapon=None, new_health=None):
    # Resetting the player count and copying values that are frame specific.
    old_values = \
        {"Position Player 1": game.player1.position,
        "Position Player 2": game.player2.position,
        "Health Player 1": game.player1.health,
        "Health Player 2": game.player2.health,
        "Coin Balance": game.player1.coin_balance,
        "Old Weapon": game.player1.current_weapon,
        "Player 1 Number": game.player1.player_number,
        "Player 2 Number": game.player2.player_number,
        }

    game.player_sprite_group.empty()

    # Creating new versions of each player if they exist
    if game.player1:
        if new_weapon:
            game.player1 = player(new_weapon)
        else:
            game.player1 = player()
        game.player1.position = old_values["Position Player 1"]
        game.player1.health = new_health if new_health else old_values["Health Player 1"]
        game.player1.coin_balance = old_values["Coin Balance"]
        game.player1.current_weapon = old_values["Old Weapon"]
        game.player1.player_number = old_values["Player 1 Number"]
        print("running recreation")
        game.player_sprite_group.add(game.player1)
        # game.update_player_sprite_group([game.player1])

    print(game.player2)
    if game.player2 == None:
        print("No second player")
    else:
        if new_weapon:
            game.player2 = player(new_weapon)
        else:
            game.player2 = player()
        game.player2.position = old_values["Position Player 2"]
        game.player2.health = new_health if new_health else old_values["Health Player 1"]
        game.player2.coin_balance = old_values["Coin Balance"]
        if new_weapon:
            game.player2.current_weapon = new_weapon
        game.player2.current_weapon = old_values["Old Weapon"]
        game.player2.player_number = old_values["Player 2 Number"]
        print("running recreation")
        game.player_sprite_group.add(game.player2)

        # game.update_player_sprite_group([game.player1, game.player2])

def yes(price, name, item_info, item_type,
        purchase_surface, players_list,
        image_path, selected_item, class_name, instance_name):
    # player_button_clicked_state tracks whether the players have been initialized.
    # if they have not, running this block will cause an error because the players
    # default to none. To access the most recent value of this attribute, we import it
    # when the function is called.
    if game.player_button_clicked_state:
        if all(p.coin_balance >= price for p in players_list):
            for p in players_list:
                p.coin_balance -= price
                print(f"{name.title()} was bought from the item shop. New Player Balance: {p.coin_balance}")

                # If a ship item is clicked, health, velocity and sprite image are updated.
                if item_type == "ships":
                    print("running ship")
                    p.health = item_info.get("Health")
                    new_movement_speed = item_info.get("Velocity")
                    new_player_sprite_path = image_path
                    print(new_player_sprite_path)
                    update_json("players", Movement_Speed=new_movement_speed)
                    update_json("players", Sprite=new_player_sprite_path)
                    recreate_players()
                # If weapon is selected, the type of bullet shot is changed.
                # So is the damage and speed. In progress.
                elif item_type == "weapons":
                    current_weapon = p.current_weapon
                    print(f"Current weapon: {current_weapon}")
                    p.current_weapon = name
                    new_weapon = p.current_weapon
                    print("blasters running")
                    recreate_players(new_weapon)
                    print(f"New Weapon = {new_weapon}")


                # Updating player attributes when an upgrade is bought.
                elif item_type == "upgrades":
                    print("running upgrades")

                    # Damage Increases
                    weapon_name = p.current_weapon
                    damage = p.all_weapons[weapon_name]["Damage"]
                    print(f"Current damage: {damage}")
                    damage_increase = item_info.get("Damage Increase", 0) # Defaulting to 0 if no value is provided.
                    update_json("weapons", Damage=(damage + damage_increase))
                    new_damage = read_json("weapons", "damage")
                    print(f"New Damage: {new_damage}\n")

                    # Health Increases
                    print(f"Current health: {p.health}")
                    p.health += item_info.get("Health Increase", 0)
                    print(f"New health: {p.health}\n")

                    # Movement speed increases
                    Movement_Speed = p.MOVEMENT_SPEED
                    print(f"Current Movement Speed: {Movement_Speed}")
                    movement_increase = item_info.get("Movement Speed Increase", 0)
                    update_json("players", Movement_Speed=(Movement_Speed + movement_increase))
                    updated_movement_speed = read_json("players", "Movement_Speed")
                    print(f"New Movement Speed: {updated_movement_speed}")
                    recreate_players()

            close_purchase(class_name, "purchase_background_visibility")
            instance_name.item_purchased = True

        # If the player does not have enough money, a notice is returned and the purchase closed.
        else:
            message = "Not enough money to purchase this item"
            font = pygame.font.SysFont('Courier New', 15, True, False)
            text = font.render(message, True, WHITE)
            purchase_surface.blit(text, (30, 30))
            close_purchase(class_name, "purchase_background_visibility")

def no(class_name):
    close_purchase(class_name, "purchase_background_visibility")

def equip():
    pass



def close_equipping(class_name, visibility):
    setattr(class_name, visibility, False)
