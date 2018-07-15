import random

class TicTacToe:

    def __init__(self):
        self.board = [' '] * 10

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

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == letter and self.board[8] == letter and self.board[9] == letter) or  # across the top
                (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter) or  # across the middle
                (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter) or  # across the bottom
                (self.board[7] == letter and self.board[4] == letter and self.board[1] == letter) or  # down the left side
                (self.board[8] == letter and self.board[5] == letter and self.board[2] == letter) or  # down the middle
                (self.board[9] == letter and self.board[6] == letter and self.board[3] == letter) or  # down the right side
                (self.board[7] == letter and self.board[5] == letter and self.board[3] == letter) or  # diagonal
                (self.board[9] == letter and self.board[5] == letter and self.board[1] == letter))  # diagonal

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 1
        else:
            return 2


print('Welcome to Tic Tac Toe!')

while True:
    # Makes game object
    game = TicTacToe()
    turn = game.whoGoesFirst()
    print('Player ' + str(turn) + ' will go first.')
    gameIsPlaying = True
    #player one is O, player 2 is X

    while gameIsPlaying:
        if turn == 1:
            # Player 1 turn.
            game.drawBoard()
            move = game.getPlayerMove()
            game.makeMove('O', move)

            if game.isWinner('O'):
                game.drawBoard()
                print('Player 1 has won the game.')
                gameIsPlaying = False
            else:
                if game.isBoardFull():
                    game.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 2

        else:
            # Player 2 turn.
            game.drawBoard()
            move = game.getPlayerMove()
            game.makeMove('X', move)

            if game.isWinner('X'):
                game.drawBoard()
                print('Player 2 has won the game.')
                gameIsPlaying = False
            else:
                if game.isBoardFull():
                    game.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 1

    if not game.playAgain():
        break
