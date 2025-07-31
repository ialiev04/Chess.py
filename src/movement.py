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
	...

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
	game.board[game.selected.pos[0]][game.selected.pos[1]] = PieceStruct("none", False, None, [old_row, old_col])
	
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