
class tictactoe(object):
	def __init__ (self):
		self.ROWS = 3
		self.COLS = 3 
		self.move_count = 0
		self.winner = 0
		self.game_over = False
		self.valid_move = False
		self.player_1_spots = []
		self.player_2_spots = []
		self.board = [[str(0) for r in xrange(self.ROWS)] for c in xrange(self.COLS)]
		self.three_in_a_row = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]

	def player_move(self, player, row, col):
		row -= 1
		col -= 1
		if self.board[row][col] == '0':
			if player == 1:
				self.board[row][col] = 'X'
				if player == 1:
					self.player_1_spots.append(self.two_to_one_d_position(row,col))
					self.player_1_spots.sort()  
					self.move_count += 1 
					return
			else:
				self.board[row][col] = 'O'	
				if player == 1:
					self.player_1_spots.append(self.two_to_one_d_position(row,col))
					self.player_1_spots.sort()  
					self.move_count += 1 
					return
			self.valid_move = True
		else:
			print('Already occupied') 

	def two_to_one_d_position(self, r, c):
		return (3 * r) + c + 1

	def check_winner(self, player):
		if player == 1:
			player_spots = self.player_1_spots
		else:
			player_spots = self.player_2_spots		
		number_of_spots = len(player_spots)
		for i in range (0,len(player_spots) - 2):
				three_spots = [player_spots[i], player_spots[i+1], player_spots[i+2]]
				#print three_spot
				if three_spots in self.three_in_a_row:
						self.winner = player
						self.game_over = True
						return 

	def __str__ (self):
		output = ''
		for row in range(self.ROWS):
			output = output + '|'.join(self.board[row])  + '\n' + '-|-|-' + '\n'
		return output

def playgame():
	#create board
	ttt = tictactoe()
	print str(ttt)
	player_alternater = 1
	while not ttt.game_over: 
		ttt.valid_move = False
		while not ttt.valid_move:
			#alternate player move input
			player_move = raw_input('Player ' + str(player_alternater) + ' choose your spot ')
			x, y = int(player_move[0]), int(player_move[2])
			ttt.player_move(player_alternater, x, y)
			print str(ttt)
		if player_alternater == 1:
			player_alternater = 2
		elif player_alternater == 2:
			player_alternater = 1

playgame()
