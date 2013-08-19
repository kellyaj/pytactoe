class InputOutput(object):

    def __init__(self, chosen_output, chosen_input):
        self.output = chosen_output
        self.input = chosen_input

    def present(self, message):
        print message

    def get_input(self):
        return raw_input()
