import tkinter as tk
from init import *
from event import *
from display import *
from movement import *

root = tk.Tk()
window_init(root)
game = game_init()
display_game(root, game)
event_listener(root, game)