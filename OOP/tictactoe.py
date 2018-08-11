class node(object):
	def __init__(self, value, next):
		self.value = 0 
		self.next = next

class linkedlist(node):
	def __init__(self)

class tictactoe(object):
	def __init__ (self):
		self.game_over = False
		self.move_count = 0 
		self.winner = 0
		self.board = self.empty_board()
		self.player_1_spots = []
		self.player_2_spots = []

	def player_move(self, player, row, col):
		if player == 1:
			if self.board[row][col] == ' ' :
				self.board[row][col] = 'X'
				self.player_1_spots.append(two_to_one_d_position(row,col)).sort()  
				self.move_count += 1 
				return
			else:
				print('Already occupied')

	def empty_board(self):
		self.ROWS = 3
		self.COLS = 3 
		[[0 for r in xrange(self.ROWS)] for c in xrange(self.COLS)]

	def two_to_one_d_position(self, tuple):
		r,c = tuple
		return (3 * r) + c 

	def check_winner(self, player_spots):
		counter = 0
		while counter > 3:
			if spot == 0:
			elif spot == 1:
			elif spot == 1:
	def __str__ (self):
		output = ''
		for row in range(self.ROWS):
			output = output + '|'.join(self.board[row])  + '\n' + '-|-|-' + '\n'
		return output
ttt = tictactoe()
print str(ttt)

def playgame():
	#create board
	ttt = tictactoe()
	print str(ttt)
	#alternate player move input
	player_1_move = raw_input('Player 1 choose your spot')
	#rerender board
	player_2_move = raw_input('Player 2 choose your spot')
