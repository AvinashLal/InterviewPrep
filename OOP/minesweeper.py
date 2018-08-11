import random 
import sys
class Minesweeper(object):
	"""docstring for Minesweeper"""
	def __init__(self, rows, cols, total_bombs=None):
		self.rows, self.cols = rows, cols
		self.game_over = False
		self.game_won = False
		self.total_bombs = 0 
		self.cells_revealed = 0 
		if not total_bombs or total_bombs > (rows * cols):
			self.total_bombs =  (rows + cols + 10) / 10
		self.bomb_map = [[0 for r in xrange (rows)] for c in xrange(cols)]
		self.answer_map = [[0 for r in xrange (rows)] for c in xrange(cols)]
		self.revealed_map = [['-' for r in xrange (rows)] for c in xrange(cols)]
		for i in xrange(self.total_bombs):
			bombRow, bombCol = random.randint(0,rows - 1), random.randint(0 ,cols - 1)
			self.bomb_map[bombRow][bombCol] = 1
			for row in [bombRow - 1, bombRow, bombRow + 1]:
				if row >= 0 and row <= self.rows - 1:
					for col in [bombCol - 1, bombCol, bombCol + 1]:
						if col >= 0 and col <= self.cols - 1:
							self.answer_map[row][col] += 1
						else:
							continue
				else:
					continue 

	def mark_cell(self, row, col):
		row -= 1
		col -= 1
		if self.revealed_map[row][col] == '-':
			if self.bomb_map[row][col]:
				self.revealed_map[row][col] = 'B'
				self.game_over = True 
				return 
			else:
				self.revealed_map[row][col] =  self.answer_map[row][col]
				self.cells_revealed += 1
				if self.cells_revealed + self.total_bombs == self.rows * self.cols:
					self.game_over = True 
					self.game_won = True
					return
		elif self.revealed_map[row][col]:
			print('Already Revealed')
			return 


	def __str__(self):
		output = ''
		for row in xrange(self.rows):
			output = output + " ".join(str(self.revealed_map[row])) + '\n'
		return output

def play_game():
	ms = Minesweeper(4,4)
	print str(ms)
	while(not ms.game_over):
		x = raw_input('Please input row,col of cell you would like to sweep \n')	
		a, b = int(x[0]), int(x[2])
		ms.mark_cell(a,b)
		print str(ms)
	if ms.game_won:
		print('You win!')
	else:
		print('You Lose! :(')

play_game()		