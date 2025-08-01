import tkinter as tk
from PIL import Image, ImageTk

class PieceStruct():
	def __init__(self, name, color, image, pos):
		self.piece: str = name
		self.color: bool = color # true is black, false is white
		self.piece_id: int = 0
		self.pos = pos
		if (image != None):
			self.photo: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(image))
class GameStruct():
	def __init__(self):
		self.board = [[0 for _ in range(8)] for _ in range(8)]
		self.state = {"mode": "select"}
		self.selected = PieceStruct(None, None, None, None)

def	window_init(root):

	chess_image = Image.open("../png/board.png")
	chess_photo = ImageTk.PhotoImage(chess_image)

	width, height = chess_image.size
	root.geometry(f"{width}x{height}")
	root.resizable(False, False)
	
	root.canvas = tk.Canvas(root, width=width, height=height)
	root.canvas.pack()
	
	root.canvas.create_image(0, 0, anchor='nw', image=chess_photo)

	root.chess_photo = chess_photo
	root.title("Chess")

def	game_init():
	game = GameStruct()
	game.board[0][0] = PieceStruct("rook", True, "../png/pieces/brook.png", [0, 0])
	game.board[0][1] = PieceStruct("knight", True, "../png/pieces/bknight.png", [0, 1])
	game.board[0][2] = PieceStruct("bishop", True, "../png/pieces/bbishop.png", [0, 2])
	game.board[0][3] = PieceStruct("queen", True, "../png/pieces/bqueen.png", [0, 3])
	game.board[0][4] = PieceStruct("king", True, "../png/pieces/bking.png", [0, 4])
	game.board[0][5] = PieceStruct("bishop", True, "../png/pieces/bbishop.png", [0, 5])
	game.board[0][6] = PieceStruct("knight", True, "../png/pieces/bknight.png", [0, 6])
	game.board[0][7] = PieceStruct("rook", True, "../png/pieces/brook.png", [0, 7])
	for i in range(8):
		game.board[1][i] = PieceStruct("pawn", True, "../png/pieces/bpawn.png", [1, i])
	game.board[7][0] = PieceStruct("rook", False, "../png/pieces/wrook.png", [7, 0])
	game.board[7][1] = PieceStruct("knight", False, "../png/pieces/wknight.png", [7, 1])
	game.board[7][2] = PieceStruct("bishop", False, "../png/pieces/wbishop.png", [7, 2])
	game.board[7][3] = PieceStruct("queen", False, "../png/pieces/wqueen.png",  [7, 3])
	game.board[7][4] = PieceStruct("king", False, "../png/pieces/wking.png", [7, 4])
	game.board[7][5] = PieceStruct("bishop", False, "../png/pieces/wbishop.png", [7, 5])
	game.board[7][6] = PieceStruct("knight", False, "../png/pieces/wknight.png", [7, 6])
	game.board[7][7] = PieceStruct("rook", False, "../png/pieces/wrook.png", [7, 7])
	for i in range(8):
		game.board[6][i] = PieceStruct("pawn", False, "../png/pieces/wpawn.png", [6, i])
	for i in range(2, 6):
		for j in range (8):
			game.board[i][j] = PieceStruct("none", None, None, [i, j])

	return game
