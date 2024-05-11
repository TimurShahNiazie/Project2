import random
import json

HIT_CHANCE = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

TEMP = 0


class Player:

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.inventory = []
        self.strength = 100
        self.health = 100
        self.weapon_multiplier = 1
        self.armour_multiplier = 1
        self.level = 1
        self.experience = 0

    def attack(self, enemy) -> None:
        """
        How much damage the player randomly does to the enemy
        :param enemy:
        :return:
        """
        if random.choice(HIT_CHANCE) == 1:
            enemy.health -= int(self.strength * random.uniform(0.05, 0.1) * self.weapon_multiplier)
            print("You hit the enemy!")
        else:
            print("You missed!")

    def rest(self) -> None:
        """
        when at the inn, rest restores the players health to full
        :return:
        """
        self.health = 100

    def gain_experience(self, amount) -> None:
        """
        Keeps track of how much experience the player
        gains from beating enemies and how many levels
        they gain from it
        :param amount:
        :return:
        """
        self.experience += amount
        if self.experience >= self.level * 100:
            self.experience -= self.level * 100
            self.level_up()

    def level_up(self) -> None:
        """
        Leveling up allows the player to do more damage
        to enemies
        :return:
        """
        self.level += 1
        self.strength += 10
        print(f"{self.name} leveled up! Level: {self.level}, Strength: {self.strength}\n")

    def save_to_json(self, file_path="player_data.json"):
        """
        saves player information to a json file
        :param file_path:
        :return:
        """
        data = {
            "name": self.name,
            "money": self.money,
            "inventory": self.inventory,
            "strength": self.strength,
            "health": self.health,
            "weapon_multiplier": self.weapon_multiplier,
            "armour_multiplier": self.armour_multiplier,
            "level": self.level,
            "experience": self.experience
        }

        with open(file_path, "w") as file:
            json.dump(data, file)

    def load_from_json(self, file_path="player_data.json"):
        """
        opens and reads the json file where the information
        was saved and uses that information for the game
        :param file_path:
        :return:
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.name = data["name"]
                self.money = data["money"]
                self.inventory = data["inventory"]
                self.strength = data["strength"]
                self.health = data["health"]
                self.weapon_multiplier = data["weapon_multiplier"]
                self.armour_multiplier = data["armour_multiplier"]
                self.level = data["level"]
                self.experience = data["experience"]
            return "successful"
        except FileNotFoundError:
            print("No saved data found.\n")
            return "failed"



class Animal:

    def __init__(self):
        """
        initalizes the animal
        """
        self.name = "Animal"
        self.strength = 50
        self.health = 50
        self.level = 1
        self.money = 5

    def attack(self, player) -> None:
        """
        How much damage the animal randomly does to the player
        :param player:
        :return:
        """
        if random.choice(HIT_CHANCE) == 1:
            damage = int(self.strength * random.uniform(0.05, 0.1))
            damage = int(damage * player.armour_multiplier)
            player.health -= damage
            print("The enemy hit you!")
        else:
            print("The enemy missed!")


class Soldier:

    def __init__(self):
        """
        initalizes the solider
        """
        self.name = "Solider"
        self.strength = 100
        self.health = 100
        self.level = 3
        self.money = 20

    def attack(self, player) -> None:
        """
        How much damage the solider does to the player
        :param player:
        :return:
        """
        if random.choice(HIT_CHANCE) == 1:
            damage = int(self.strength * random.uniform(0.05, 0.1))
            damage = int(damage * player.armour_multiplier)
            player.health -= damage
            print("The enemy hit you!")
        else:
            print("The enemy missed!")


class Giant:

    def __init__(self):
        """
        initalizes the giant
        """
        self.name = "Giant"
        self.strength = 200
        self.health = 200
        self.level = 5
        self.money = 50

    def attack(self, player) -> None:
        """
        How much damage the giant randomly does to the player
        :param player:
        :return:
        """
        if random.choice(HIT_CHANCE) == 1:
            damage = int(self.strength * random.uniform(0.05, 0.1))
            damage = int(damage * player.armour_multiplier)
            player.health -= damage
            print("The enemy hit you!")
        else:
            print("The enemy missed!")