import random
class Game():
    Game_List=["Minecraft","Call Of Duty","Fortnate","PUPG"]

    def select_game(self):
        self.Pc_Game=random.choice(self.Game_List)
        print(self.Pc_Game)

    def check(self):
        if self.Pc_Game == "Minecraft":
            input("Enter Make Year Of Minecraft:")

        elif self.Pc_Game == "Call Of Duty":
            input("Enter Make Year Of Call Of Duty:")

        elif self.Pc_Game == "Fortnate":
            input("Enter Make Year Of Fortnate:")

        elif self.Pc_Game == "PUPG":
            input("Enter Make Year Of PUPG:")

g=Game()
g.select_game()
g.check()
