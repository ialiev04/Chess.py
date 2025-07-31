from init import *

def	map_coords(i, j):
	x = j * 100 + 49
	y = i * 100 + 49
	return (x, y)
	

def	display_game(root, game):
	for i in range (8):
		for j in range (8):
			if game.board[i][j].piece != "none":
				x, y = map_coords(i, j)
				game.board[i][j].piece_id = root.canvas.create_image(x, y, image=game.board[i][j].photo)
