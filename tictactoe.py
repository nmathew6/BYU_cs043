class TicTacToe():

    def __init__(self, letter):
        self.board = [' '] * 10
        self.letter = letter

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        self.board = bo
        self.letter = le
        return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or  # across the top
                (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or  # across the middle
                (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or  # across the bottom
                (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or  # down the left side
                (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or  # down the middle
                (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or  # down the right side
                (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or  # diagonal
                (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter))  # diagonal

    def getPlayerMove(self, board):
        # Let the player type in his move.
        self.board = board
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(self.board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def makeMove(self, move):
        self.move = move
        self.board[self.move] = self.letter

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(self.board, i):
                return False
        return True

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        self.board = board
        self.move = move
        return self.board[self.move] == ' '

