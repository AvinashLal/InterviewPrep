import random 

class Minesweeper(object):
	"""docstring for Minesweeper"""
	def __init__(self, rows, cols, total_bombs=None):
		self.rows, self.cols = rows, cols
		self.game_over = False
		self.game_won = False
		self.total_bombs = 0 
		self.bomb_map = [[0 for r in xrange (rows)] for c in xrange(cols)]
		self.answer_map = [[0 for r in xrange (rows)] for c in xrange(cols)]
		self.revealed_map = [[0 for r in xrange (rows)] for c in xrange(cols)]
		if not total_bombs:
			self.total_bombs =  (rows + cols + 10) / 10 
		for i in xrange(self.)

	def mark_cell(self, row, col):
		if not self.revealed_map[row][col]:
			if self.bomb_map[row][col]:
				self.game_over = True 
			else:
				self.revealed_map[row][col] =  self.answer_map[row][col]

		elif self.revealed_map[row][col]:
			return 


	def __str__(self):



Minesweeper(4, 4)
		