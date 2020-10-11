testSudoku =	[[4, 0, 0, 0, 0, 5, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 1, 9, 8],
				[3, 0, 0, 0, 8, 2, 4, 0, 0],
				[0, 0, 0, 1, 0, 0, 0, 8, 0],
				[9, 0, 3, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 3, 0, 6, 7, 0],
				[0, 5, 0, 0, 0, 9, 0, 0, 0],
				[0, 0, 0, 2, 0, 0, 9, 0, 7],
				[6, 4, 0, 3, 0, 0, 0, 0, 0]]


def findEmpty(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return [i, j]

def validForRow(pos, num, sudoku):
	for i in range(0,9):
		if num == sudoku[pos[0]][i]:
			return False
	return True

def validForColumn(pos, num, sudoku):
	for i in range(0,9):
		if num == sudoku[i][pos[1]]:
			return False
	return True

def squareFromCoords(pos, sudoku):
	square = []

	xSquare = (pos[1] // 3) * 3
	ySquare = (pos[0] // 3) * 3

	for i in range(3):
		square.append(sudoku[ySquare + i][xSquare:xSquare + 3])

	return square

def validForSquare(pos, num, sudoku):
	square = squareFromCoords(pos, sudoku)
	for i in range(3):
		for j in range(3):
			if num == square[j][i]:
				return False
	return True

def validForAll(pos, num, sudoku):
	return validForRow(pos, num, sudoku) and validForColumn(pos, num, sudoku) and validForSquare(pos, num, sudoku)

def solve(sudoku):
	foundEmpty = findEmpty(sudoku)
	if not foundEmpty:
		return True
	else:
		row, col = foundEmpty

	for i in range(1, 10):
		if validForAll((row, col), i, sudoku):
			sudoku[row][col] = i

			if solve(sudoku):
				return True
			else:
				sudoku[row][col] = 0

	return False

def printBoard(sudoku):
	for i in range(9):
		if i % 3 == 0 and i != 0:
			print('-----------------------')

		for j in range(9):
			if j % 3 == 0 and j != 0:
				print(' | ', end='')

			if j == 8:
				print(sudoku[i][j])
			else:
				print(str(sudoku[i][j]) + ' ', end = '')