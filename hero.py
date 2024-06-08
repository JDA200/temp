from enemies import Colors, Enemy
import misc_funcs as ms
import random

ENEMY_COLOR = Colors.RED
ITEM_COLOR = Colors.GOLD
HERO_COLOR = Colors.BLUE
HP_COLOR = Colors.GREEN
RESET_COLOR = Colors.RESET

class Hero:
    def __init__(self):
        self.name = input('Name your hero!:\n')
        self.health = 30
        self.item = {"name" : "unarmed", "damage" : 20}
        self.alive = True
        self.inventory = {"Gold" : 0,
                          "Items" : []}
        print(f"{HERO_COLOR + self.name + RESET_COLOR}\nHP - {HP_COLOR + str(self.health) + RESET_COLOR}\nItem - {ITEM_COLOR + self.item['name'] + RESET_COLOR}")
        ms.pause()



    def attack(self):
        item = self.item
        potential_dmg = random.randint(-5, 5) + item["damage"]
        if potential_dmg <= 0:
            actual_dmg = 1
        else:
            actual_dmg = potential_dmg
        print(f"{HERO_COLOR + self.name +RESET_COLOR} attacks with {ITEM_COLOR + self.item['name'] + RESET_COLOR}, dealing {actual_dmg} damage!")
        ms.pause()
        return actual_dmg

    def death(self):
        print(f"{self.name} has been defeated!")
        self.alive == False
        ms.pause()

    def health_update(self):
        print(f"{HERO_COLOR + self.name + RESET_COLOR} has {HP_COLOR + str(self.health) + RESET_COLOR} HP")
        ms.pause()
        return ""

    def take_dmg(self, damage_taken):
        temp_health = self.health
        temp_health -= damage_taken
        if temp_health <= 0:
            self.alive = False
            self.death()
        else:
            self.health = temp_health
            print(f"{HERO_COLOR + self.name + RESET_COLOR} takes {damage_taken} points of damage!", end='. ')
            self.health_update()


if __name__ == "__main__":
    def hero_fight_sim():
        hero1 = Hero()
        hero2 = Hero()
        while hero1.alive and hero2.alive:
            damage = hero1.attack()
            hero2.take_dmg(damage)
            if hero1.alive and hero2.alive:
                damage = hero2.attack()
                hero1.take_dmg(damage)

    def hero_fight_enemy_sim():
        hero = Hero()
        while hero.alive:
            enemy = Enemy()
            while enemy.alive:
                damage = hero.attack()
                enemy.take_dmg(damage)
                if enemy.alive:
                    damage = enemy.attack()
                    hero.take_dmg(damage)
                elif enemy.alive == False:
                    hero.inventory["Gold"] += enemy.loot["gold"]
                    hero.inventory["Items"] += [enemy.loot["item_drop"]] if enemy.loot["item_drop"] is not None else hero.inventory["Items"]
                    print(f"\nInventory:\n"
                          f"\tGold: {ITEM_COLOR + str(hero.inventory['Gold']) + RESET_COLOR}\n"
                          f"\tItems: {hero.inventory}")
                    ms.pause()


    hero_fight_enemy_sim()

