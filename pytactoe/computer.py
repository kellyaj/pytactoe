from player import Player

class Computer(Player):

    def __init__(self, mark):
        super(Computer, self).__init__(mark)

    def get_move(self, presenter, available_spots):
        presenter.computer_move_message()
        return available_spots[0]
