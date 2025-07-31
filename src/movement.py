import tkinter as tk
from init import *
from event import *
from display import *

def	capture_piece(root, game, row, col):
	root.canvas.delete(game.board[row][col].piece_id)
	move_piece(root, game, row, col)
	

def	play_pawn(root, game, row, col):
	...

def	play_rook(root, game, row, col):
	rook = game.selected
	cur_y = rook.pos[0]
	cur_x = rook.pos[1]
	if (cur_y == row and cur_x == col):
		return
	elif ((cur_y != row and cur_x == col) or (cur_y == row and cur_x != col)):
		if (cur_y != row):
			start = min(cur_y, row)
			end = max(cur_y, row)
			for i in range(start + 1, end):
				if game.board[i][col].piece != "none":
					return
		else:
			start = min(cur_x, col)
			end = max(cur_x, col)
			for i in range(start + 1, end):
				if game.board[row][i].piece != "none":
					return
	else:
		return
	if (game.board[row][col].color == game.selected.color):
		return
	else:
		if (game.board[row][col].color == None):
			move_piece(root, game, row, col)
		else:
			capture_piece(root, game, row, col)

def	play_knight(root, game, row, col):
	...

def	play_bishop(root, game, row, col):
	...

def	play_king(root, game, row, col):
	...

def	play_queen(root, game, row, col):
	...

def	move_piece(root, game, row, col):
	root.canvas.delete(game.selected.piece_id)

	old_col = game.selected.pos[0]
	old_row = game.selected.pos[1]
	game.board[game.selected.pos[0]][game.selected.pos[1]] = PieceStruct("none", None, None, [old_row, old_col])
	
	game.board[row][col] = game.selected
	game.selected.pos = [row, col]

	x = col * 100 + 49
	y = row * 100 + 49
	game.board[row][col].piece_id = root.canvas.create_image(x, y, image=game.board[row][col].photo)

def	validate_piece_mov(root, game, row, col):
	if (game.selected.piece == "pawn"):
		play_pawn(root, game, row, col)
	elif (game.selected.piece == "rook"):
		play_rook(root, game, row, col)
	elif (game.selected.piece == "knight"):
		play_knight(root, game, row, col)
	elif (game.selected.piece == "bishop"):
		play_bishop(root, game, row, col)
	elif (game.selected.piece == "queen"):
		play_queen(root, game, row, col)
	elif (game.selected.piece == "king"):
		play_king(root, game, row, col)
	game.state["mode"] = "select"