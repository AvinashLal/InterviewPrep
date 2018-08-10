# x = [[0 for r in xrange(3+2)] for r in xrange(3+2)]
# print(x) 

  # def __str__(self):
  #   line1, line2, line3 = "    ", "    ", "    "
  #   for c in xrange(1, self.cols+1):
  #     label = str(c)
  #     while len(label) < 3:
  #       label = " " + label
  #     line1 += " " + label[0]
  #     line2 += " " + label[1]
  #     line3 += " " + label[2]
  #   parts = [line1, '\n', line2, '\n', line3, '\n']
  #   parts.append(('   +' + '-' * (2*self.cols+1)) + '+\n')
  #   for r in xrange(1, self.rows+1):
  #     label = str(r)
  #     while len(label) < 3:
  #       label = " " + label
  #     parts += label + '| '
  #     for c in xrange(1, self.cols+1):
  #       if self.revealed[r][c]:
  #         if self.bombs[r][c]:
  #           parts.append("B ")
  #         elif self.counts[r][c]:
  #           parts.append(str(self.counts[r][c]) + " ")
  #         else:
  #           parts.append("  ")
  #       else:
  #         parts.append(". ")
  #     parts += '|\n'
  #   parts += ['   +' + ('-' * (2*self.cols+1)) + '+\n']
  #   return "".join(parts)

word = ['words', 'with', 'friends']
print(" ".join(word))