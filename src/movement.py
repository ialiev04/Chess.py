import tkinter as tk
from init import *
from event import *
from display import *

def	capture_piece(root, game, row, col):
	root.canvas.delete(game.board[row][col].piece_id)
	move_piece(root, game, row, col)

def	play_pawn(root, game, row, col):
	pawn = game.selected
	cur_y = pawn.pos[0]
	cur_x = pawn.pos[1]

	if (cur_y == row and cur_x == col):
		return

	#first time movers
	if (abs(row - cur_y) == 2 and col == cur_x):
		y_dir = 1 if pawn.color == True else -1
		if ((pawn.color == False and cur_y == 6) or (pawn.color == True and cur_y == 1)):
			if (game.board[row][col].piece == "none" and game.board[row + y_dir][col].piece == "none"):
				move_piece(root, game, row, col)
		else:
			return

	#seasoned movers
	elif (abs(row - cur_y) == 1 and col == cur_x):
		if ((pawn.color == False and row - cur_y == -1) and game.board[row][col].piece == "none"):
			move_piece(root, game, row, col)
		elif ((pawn.color == True and row - cur_y == 1)and game.board[row][col].piece == "none"):
			move_piece(root, game, row, col)
		else:
			return
			


def	play_rook(root, game, row, col):
	rook = game.selected
	cur_y = rook.pos[0]
	cur_x = rook.pos[1]

	if (cur_y == row and cur_x == col):
		return

	if ((cur_y != row and cur_x == col) or (cur_y == row and cur_x != col)):
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
	knight = game.selected
	cur_y = knight.pos[0]
	cur_x = knight.pos[1]
	if (cur_y == row and cur_x == col):
		return
	if ((abs(cur_y - row) == 2 and abs(cur_x - col) == 1) or (abs(cur_y - row) == 1 and abs(cur_x - col) == 2)):
		if (game.board[row][col].color != knight.color):
			if (game.board[row][col].color == None):
				move_piece(root, game, row, col)
			else:
				capture_piece(root, game, row, col)
		else:
			return
	else:
		return

def	play_bishop(root, game, row, col):
	bishop = game.selected
	cur_y = bishop.pos[0]
	cur_x = bishop.pos[1]

	if (cur_y == row and cur_x == col):
		return
	if (abs(cur_y - row) == abs(cur_x - col)):
		y_dir = 1 if row < cur_y else -1
		x_dir = 1 if col < cur_x else -1
		check_y = row
		check_x = col
		for i in range(abs(row - cur_y) - 1):
			check_y += y_dir
			check_x += x_dir
			if (game.board[check_y][check_x].piece != "none"):
				return
	else:
		return
	if (game.board[row][col].color != bishop.color):
		if (game.board[row][col].color == None):
			move_piece(root, game, row, col)
		else:
			capture_piece(root, game, row, col)
	else:
		return


def	play_king(root, game, row, col):
	king = game.selected
	cur_y = king.pos[0]
	cur_x = king.pos[1]
	if (cur_y == row and cur_x == col):
		return
	if (abs(cur_y - row) == 1 or abs(cur_x - col) == 1):
		if (game.board[row][col].color != king.color):
			if (game.board[row][col].color == None):
				move_piece(root, game, row, col)
			else:
				capture_piece(root, game, row, col)
	else:
		return


def	play_queen(root, game, row, col):
	queen = game.selected
	cur_y = queen.pos[0]
	cur_x = queen.pos[1]
	if (cur_y == row and cur_x == col):
		return
	if (abs(cur_y - row) == abs(cur_x - col) or ((cur_y != row and cur_x == col) or (cur_y == row and cur_x != col))):
		if (cur_y != row and cur_x == col) or (cur_y == row and cur_x != col):	#rook logic
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
		elif (abs(cur_y - row) == abs(cur_x - col)):	#bishop logic
			if (abs(cur_y - row) == abs(cur_x - col)):
				y_dir = 1 if row < cur_y else -1
				x_dir = 1 if col < cur_x else -1
				check_y = row
				check_x = col
				for i in range(abs(row - cur_y) - 1):
					check_y += y_dir
					check_x += x_dir
					if (game.board[check_y][check_x].piece != "none"):
						return
			else:
				return
				
	if (game.board[row][col].color != queen.color):
		if (game.board[row][col].color == None):
			move_piece(root, game, row, col)
		else:
			capture_piece(root, game, row, col)
	else:
		return

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


	#knight sometimes doesnt capture when in row(0)
	#king moves like knight sometimes?!