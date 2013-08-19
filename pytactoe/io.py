class InputOutput(object):

    def __init__(self, chosen_output, chosen_input):
        self.chosen_output = chosen_output
        self.chosen_input = chosen_input

    def present(self, message):
        self.chosen_output.write(message + "\n")

    def get_input(self):
        return self.chosen_input.readline()
