import random
import os
from entityLogic import *

random_wild_encounter = [1,1,2,2,3,3,4,5,5,6]
shard_no = 0

class Game:
    def __init__(self) -> None:
        """
        Turns on the game!
        """
        self.game_on = True




    def start(self) -> None:
        """
        Checks if the game is on and establishes a new player name
        :return:
        """
        while self.game_on:
            player_name = input("What is your name adventurer?\n")
            print("Welcome " + player_name + "!\n")
            player = Player(player_name)
            self.player_alive(player)

    def player_alive(self, player) -> None:
        """
        Checks that the player is alive using a loop
         and takes in all the inputs
        from the user. All the logic is stored here
        :param player

        """
        player_alive = True
        while player_alive:
            turn_action = input("What would you like to do?\n1. Explore\n2. Check Stats\n3. Visit Inn\n4. Save Game\n5. Load Game\nYour choice: ")
            print()
            result = None

            if turn_action == "1":
                encounter = random.choice(random_wild_encounter)
                if encounter == 1:
                    print("You didn't encounter anything.\n")
                elif encounter == 2:
                    animal = Animal()
                    result = self.battle(player, animal)
                elif encounter == 3:
                    soldier = Soldier()
                    result = self.battle(player, soldier)
                elif encounter == 4:
                    giant = Giant()
                    result = self.battle(player, giant)
                elif encounter == 5:
                    result = None
                    loot_found = random.choice([0, 1])
                    if loot_found == 0:
                        money_found = random.choice([10, 20, 30, 40, 50])
                        print(f"You found {money_found} gold!\n")
                        player.money += money_found
                    elif loot_found == 1:
                        item_found = random.choice(["Leather Tunic", "Iron Shard", "Crystal Shard"])
                        print(f"You found a {item_found}!\n")
                        player.inventory.append(item_found)
                elif encounter == 6:
                    result = None
                    print("You found a ??!\n")
                    player.inventory.append("???")
            if result == "dead":
                player_alive = False
                replay = input("Would you like to play again? (y/n) ")
                if replay == "n":
                    self.game_on = False
                    break
                elif replay == "y":
                    continue
                else:
                    print("Invalid input, exiting game.")
                    self.game_on = False
                    break



            elif turn_action == "2":

                print("You look into the mirror and see...!\n")

                in_bag = True
                while in_bag:
                    player_action = input("What would you like to do?\n1. Check Stats\n2. Exit\nYour choice: ")
                    print("\n")

                    if player_action == "1":
                        print("Your stats:")
                        print(f"Health: {player.health}")
                        print(f"Level: {player.level}")
                        print(f"Experience: {player.experience}")
                        print(f"Health: {player.health}")
                        print(f"Strength: {player.strength}")
                        print(f"Weapon Multiplier: {player.weapon_multiplier}")
                        print(f"Armour Multiplier: {player.armour_multiplier}")
                        print(f"Highest Attack: {int(player.strength * player.weapon_multiplier * 0.1)}")
                        print(f"Money: {player.money}")
                        print(f"Inventory: {player.inventory}\n")
                    elif player_action == "2":
                        in_bag = False
            elif turn_action == "3":
                print("Welcome to the inn!\n")
                inn_action = input("What would you like to do?\n1. Rest(10 gold)\n2. Exit\nYour choice: ")
                print("\n")
                if inn_action == "1":
                    player.rest()
                    print("Thank you for visiting, you are fully rested!")
                    print(f"Your health is now {player.health}!\n")
                    player.money -= 10
                elif inn_action == "2":
                    pass

            elif turn_action == "4":
                player.save_to_json()
                print("Game saved.\n")
                continue


            elif turn_action == "5":
                load_result = player.load_from_json()
                if load_result == "successful":
                    print("Game loaded.\n")
                    continue
                continue

    def battle(self, player, enemy) -> str:
        """
        Makes the player and a randomly enemy fight each other.
        The chance of doing damange is random but the damage itself is
        fixed. The player is rewarded for beating the enemy and the
        game shuts off if the plauer dies
        :param player:
        :param enemy:
        :return:
        """
        print(enemy.name + " has appeared!\n")
        while player.health > 0 and enemy.health > 0:
            print("Your health: " + str(int(player.health)))
            print("Enemy health: " + str(int(enemy.health)) + "\n")
            turn_action = input("What would you like to do?\n1. Attack\n2. Run\nYour choice: ")
            print()

            if turn_action == "1":
                player.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(player)

            elif turn_action == "2":
                if random.choice([0, 0, 1]) == 1:
                    print("You ran away!\n")
                    return None
                else:
                    print("You failed to run away!\n")
                    enemy.attack(player)

        if player.health <= 0:
            print("You died!\n")
            return "dead"
        elif enemy.health <= 0:
            print(f"You defeated the {enemy.name}!\n")
            print(f"You gained {enemy.level * 10} experience!")
            print(f"You gained {enemy.money} gold!\n")
            player.money += enemy.money
            player.gain_experience(enemy.level * 10)













