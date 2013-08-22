import sys
from pytactoe.io import InputOutput
from pytactoe.game_loop import GameLoop

io = InputOutput(sys.stdout, sys.stdin)
loop = GameLoop(io)
loop.start_game()
