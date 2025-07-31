from functools import partial
from display import *
from init import *
from movement import *
from movement import validate_piece_mov

def	choose_piece(game, row, col):
	if (game.board[row][col].piece == "none"):
		return
	else:
		game.selected = game.board[row][col]
		game.state["mode"] = "move"

def	on_click(event, root, game):
		x, y = event.x, event.y
		row = y // 100
		col = x // 100
		if (game.state["mode"] == "select"):
			choose_piece(game, row, col)
		elif (game.state["mode"] == "move"):
			validate_piece_mov(root, game, row, col)

def	event_listener(root, game):
	root.canvas.bind("<Button-1>", partial(on_click, root=root, game=game))
	root.mainloop()