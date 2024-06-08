import yaml
import enemies
import hero
import misc_funcs as ms

#Initialisation
class Game:
    def __init__(self):
        self.game_text = self.load_game_text()
        self.character = hero.Hero()
        self.character["name"] = input('Name your hero!\n').strip()
        self.game_running = True


    def load_game_text(self, filename="text.yaml"):
        with open(filename, 'r') as file:
            return yaml.safe_load(file)

    def print_intro(self):
        print(self.game_text.get("intro", 'intro text not found'))

    def get_player_input(self):
        print(list(['Attack', 'Heal', 'Flee', 'quit']))
        return input("What do you want to do?\n").strip().lower()

    def handle_input(self, command):
        if command == "quit":
            self.game_running = False
            print(self.game_text["commands"]["quit"])
        elif command == "Attack":
            pass
        elif command == "open door":
            print(self.game_text["open_door"])
        elif command == "inventory":
            inventory = self.player["inventory"]
            inventory_text = self.game_text["commands"]["inventory"]
            print(f"{inventory_text}{', '.join(inventory) if inventory else self.game_text['commands']['inventory_empty']}")
        else:
            print(self.game_text["commands"]["unknown"])

    def game_loop(self):
        self.print_intro()
        ms.pause()
        enemy = enemies.Enemy()
        while self.game_running:
            command = self.get_player_input()
            self.handle_input(command)




if __name__ == "__main__":
    game = Game()
    game.game_loop()





