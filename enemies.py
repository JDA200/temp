import random
import misc_funcs as ms


class Colors:
    # ANSI escape codes for color formatting
    RED = '\033[91m'
    GOLD = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'  # Reset to default color

ENEMY_COLOR = Colors.RED
ITEM_COLOR = Colors.GOLD
HERO_COLOR = Colors.BLUE
HP_COLOR = Colors.GREEN
RESET_COLOR = Colors.RESET

enemy_values = {
    "names" : ['Kefur', 'Sigmid', 'Ozan', 'Clences', 'Prion', 'Zetoid',
         'Xylanth', 'Vorath', 'Thaldrin', 'Zarvik', 'Eldorin',
         'Grendor', 'Valdor', 'Thormar', 'Ezra', 'Baelor',
         'Xanthur', 'Fyren', 'Zael', 'Korin'],

    "titles" : ['the black', 'the greedy', 'the mighty', 'the skittish', 'the cowardly',
          'the fearless', 'the cunning', 'the wise', 'the relentless', 'the shadow',
          'the elusive', 'the merciless', 'the vigilant', 'the swift', 'the stalwart',
          'the thunderous', 'the fiery', 'the cunning', 'the wily', 'the stealthy'],

    "items" : [
        {"name": "wonky club", "damage": 10},
        {"name": "large stick", "damage": 3},
        {"name": "iron sword", "damage": 15},
        {"name": "rusty dagger", "damage": 5},
        {"name": "steel axe", "damage": 20},
        {"name": "golden spear", "damage": 25},
        {"name": "silver shield", "damage": 8},
        {"name": "magic wand", "damage": 12},
        {"name": "poisoned dart", "damage": 7},
        {"name": "enchanted staff", "damage": 18},
        {"name": "obsidian blade", "damage": 22},
        {"name": "wooden bow", "damage": 13},
        {"name": "leather armor", "damage": 6},
        {"name": "steel lance", "damage": 16},
        {"name": "diamond katana", "damage": 24},
        {"name": "dragon scale", "damage": 23},
        {"name": "ancient relic", "damage": 11},
        {"name": "toxic potion", "damage": 9},
        {"name": "mystic amulet", "damage": 14},
        {"name": "fireball scroll", "damage": 21}
    ]

}


class Enemy:
    gold: int

    def __init__(self):
        self.name = ENEMY_COLOR + random.choice(enemy_values["names"]) + " " + random.choice(enemy_values["titles"]) + RESET_COLOR
        self.alive = True
        self.health = random.randint(1, 5) * 5
        self.item = random.choice(enemy_values["items"])
        self.gold = random.randint(1, 20)
        self.item_drop = self.item if random.random() < 0.99 else None
        if self.item_drop is not None:
            self.loot = {"gold" : self.gold,
                         "item_drop" : self.item_drop}
        else:
            self.loot = {"gold" : self.gold,
                         "item_drop" : "no item"}
                     
        self.print_appearance()
        ms.pause()

    def print_appearance(self):
        print(f"{ENEMY_COLOR + self.name + RESET_COLOR} appears, wielding {ITEM_COLOR + self.item['name'] + RESET_COLOR}! HP - {HP_COLOR + str(self.health) + RESET_COLOR}")

    def death(self):
        print(f"{self.name} has been defeated!")
        self.alive == False
        ms.pause()
        self.loot_drop()
    
    def loot_drop(self):
        dropped_loot = {"gold": self.gold, "item": self.loot['item_drop'] if self.loot['item_drop'] is not None else None}
        if dropped_loot["item"] is not None:
            print(f"Loot:\n\t{ITEM_COLOR + str(self.loot['gold']) + RESET_COLOR} gold\n\t{ITEM_COLOR + self.loot['item_drop']['name'] + RESET_COLOR}")
        elif dropped_loot["item"] is None:
            print(f"Loot:\n\t{ITEM_COLOR + str(self.loot['gold']) + RESET_COLOR} gold")
            self.loot = self.loot["gold"]
        return self.loot
        

    def health_update(self):
        print(f"{ENEMY_COLOR + self.name + RESET_COLOR} has {HP_COLOR + str(self.health) + RESET_COLOR} HP")
        ms.pause()
        return ""

    def attack(self):
        item = self.item
        potential_dmg = random.randint(-5, 5) + item["damage"]
        if potential_dmg <= 0:
            actual_dmg = 1
        else:
            actual_dmg = potential_dmg

        print(f"{ENEMY_COLOR + self.name +RESET_COLOR} attacks with {ITEM_COLOR + self.item['name'] + RESET_COLOR}, dealing {actual_dmg} damage!")
        ms.pause()
        return actual_dmg

    def take_dmg(self, damage_taken):
        temp_health = self.health
        temp_health -= damage_taken
        if temp_health <= 0:
            self.alive = False
            self.death()
        else:
            self.health = temp_health
            print(f"{self.name} takes {damage_taken} points of damage!", end='. ')
            self.health_update()



#simulate 2 enemies attacking eachother
if __name__ == "__main__":
    enemy1 = Enemy()
    enemy2 = Enemy()
    while enemy1.alive == True and enemy2.alive == True:
        #e1 attacks e2
        damage = enemy1.attack()
        enemy2.take_dmg(damage)
        #e2 attacks e1
        if enemy1.alive == True and enemy2.alive == True:
            damage = enemy2.attack()
            enemy1.take_dmg(damage)
        else:
            break



