from pytactoe.player import Player

class Human(Player):

    def __init__(self, mark, io):
        super(Human, self).__init__(mark)
        self.io = io

    def get_move(self, *args):
        return self.io.get_input()
