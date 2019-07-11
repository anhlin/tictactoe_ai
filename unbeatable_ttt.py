# Anthony Lin
# Unbeatable Tic Tac Toe
# July 10, 2019

import copy

#Initialize board
def init_board():
	board = []
	for i in range(0, 3):
		col = []
		for j in range(0, 3):
			col.append(' ')
		board.append(col)
	return board

#Prints the current board state
def print_board(board):
	print('    1   2   3    ')
	print('    ---------    ')
	space = '   ' 
	for i in range(1, 4):
		row = ''
		frmt = '%s%d%s' % (' ' , i, ' |')
		row = space.join(board[i-1])
		print (frmt + row + '|')
	print('    ---------    \n')

#Error detection helper
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Checks if a move is valid
def validate_move(col, row, board):
	#Check if col and row are integers
	if(RepresentsInt(col) is False or RepresentsInt(row) is False):
		return False
	col = int(col)
	row = int(row)
	#Check if col and row are between 1 and 3 
	if not((1 <= col <= 3) and (1 <= row <= 3)):
		return False
	#Check if the space is available
	if(board[row-1][col-1] is not ' '):
		return False	
	return True

#Take row and col input from player and put it on the board if valid
def player_place(board):
	while True:
		col = input("Enter column: ")
		row = input("Enter row: ")
		print("\n")
		if validate_move(col, row, board) is True:
			board[int(row)-1][int(col)-1] = 'X'
			break
		else:
			print("Invalid move!")

def cpu_move(board):
	for i in range(0,3):
		for j in range(0,3):
			cpy = copy.deepcopy(board)
			cpy2 = copy.deepcopy(board)
			if validate_move(j+1, i+1, board) is True: 
				cpy[i][j] = 'O'
				cpy2[i][j] = 'X'
				if check_win(cpy) is True:
					board[i][j] = 'O'
					return True 
				if check_win(cpy2) is True:
					board[i][j] = 'O'
					return True
	
	if validate_move(2, 2, board) is True:
		board[1][1] = 'O'
		return True
	
	elif validate_move(1, 1, board) is True:
		board[0][0] = 'O'
		return True
	
	elif validate_move(1, 3, board) is True:
		board[0][2] = 'O' 
		return True

	elif validate_move(3, 1, board) is True:
		board[2][0] = 'O'
		return True 
	
	elif validate_move(3, 3, board) is True:
		board[2][2] = 'O'
		return True

	elif validate_move(2, 1, board) is True:
		board[1][0] = 'O' 
		return True
	
	elif validate_move(3, 2, board) is True:
		board[2][1] = 'O' 
		return True

	elif validate_move(2, 3, board) is True:
		board[1][2] = 'O'
		return True

	elif validate_move(1, 2, board) is True:
		board[0][1] = 'O' 
		return True

#Checks if someone won
def check_win(board):
	for i in range(0, 3):
		if (all(val == 'X' for val in board[i]) or all(val == 'O' for val in board[i])):
			return True
		if(board[0][i] == board[1][i] == board[2][i] != ' '):
			return True
	if(board[0][0] == board[1][1] == board [2][2] != ' '):
		return True
	if(board[0][2] == board[1][1] == board [2][0] != ' '):
		return True 

def check_draw(board):
	turns = 0 
	for i in range(0, 3):
		for j in range (0, 3):
			if board[i][j] != ' ':
				turns+=1
	if turns == 9:
		return True
		
board = init_board()
print_board(board)
while(True):
	print("Your Turn: ")
	player_place(board)
	system('clear')
	print_board(board)
	print("CPU's Turn: ")
	cpu_move(board)
	system('clear')
	print_board(board)
	
	if(check_win(board) is True):
		print_board(board)
		print("Winner!")
		break
	
	if(check_draw(board) is True):
		print_board(board)
		print("Draw!")
		break

	#cpu_turn(board)

