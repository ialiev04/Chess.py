from functools import partial
from display import *
from init import *

def	move_piece(root, game, x, y):
	root.canvas.delete(game.selected.piece_id)
	game.board[x][y] = game.selected
	game.board[game.selected.pos[0]][game.selected.pos[1]] = PieceStruct("none", False, None, [0, 0])
	display_game(root, game)
	return


def	check_move(root, game, row, col):
	game.state["mode"] = "select"
	if (game.board[row][col].piece == "none"):
		return (0)
	else:
		return (1)			#redo
	

def	choose_piece(game, x, y):
	if (game.board[x][y].piece == "none"):
		return
	else:
		game.selected = game.board[x][y]
		game.state["mode"] = "move"

def	on_click(event, root, game):
		x, y = event.x, event.y
		row = y // 100
		col = x // 100
		if (game.state["mode"] == "select"):
			choose_piece(game, row, col)
		elif (game.state["mode"] == "move"):
			if (check_move(root, game, row, col) == 0):
				move_piece(root, game, row, col)

def	event_listener(root, game):
	root.canvas.bind("<Button-1>", partial(on_click, root=root, game=game))
	root.mainloop()