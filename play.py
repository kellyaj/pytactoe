import sys
from pytactoe.io import InputOutput
from pytactoe.game_loop import GameLoop

io = InputOutput(sys.stdin, sys.stdout)
loop = GameLoop(io)
loop.start_game()
