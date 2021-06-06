## Python automation short exercise with a tic tac toe board using a dictionary

def printBoard(board):

    """Prints out a shitty version of a tic-tac-toe board"""
    
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWin(board, move):
    
    """Checks whether the move that was just inputted triggers a win."""

    if (board['top-L'] == move and board['top-M'] == move and board['top-R'] == move):                  ## This chunk of code checks for horizontal wins
        return True
    if (board['mid-L'] == move and board['mid-M'] == move and board['mid-R'] == move):
        return True
    if (board['low-L'] == move and board['low-M'] == move and board['low-R'] == move):
        return True

    if (board['top-L'] == move and board['mid-L'] == move and board['low-L'] == move):                  ## This chunk checks for vertical wins
        return True
    if (board['top-M'] == move and board['mid-M'] == move and board['low-M'] == move):
        return True
    if (board['top-R'] == move and board['mid-R'] == move and board['low-R'] == move):
        return True

    if (board['top-L'] == move and board['mid-M'] == move and board['low-R'] == move):                  ## This chunk checks for diagonal wins
        return True
    if (board['top-R'] == move and board['mid-M'] == move and board['low-L'] == move):
        return True
        


## printBoard(theBoard)            ## Tic-Tac-Toe board has been printed using a function

winFlag = False
turn = 'X'

while True:

    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',           ## Resets the board after every playthrough
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    startCommand = input("Want to start a game of Tic-Tac-Toe? (Yes to proceed): ")

    if startCommand == 'Yes':

        ## Probably where the while loop will start for playing again
        
        turn = 'X'                                      ## Starts off with 'X' going first, and then switching to 'O' if turn == 'X' and vice versa
        quitFlag = False                                ## This is the flag for checking whethero the second break occurs after the break in the while True loop
        availableSpaces = list(theBoard.keys())         ## Initial list of the available spaces, will be removed one by one
        winFlag = False                                 ## Flag for whether the game was won or not

        print("Remember that you can enter 'quit' at anytime to quit the program.")
        
        
        for i in range(9):                              ## 9 turns
            printBoard(theBoard)
            print("It's " + turn + "'s turn.")
            move = input("Which space do you want to go on? (top, mid, low): ")

            while True:                                 ## This loop checks if the move input is valid and in the pre-existing keys, otherwise loops until valid
                if move == 'quit':
                    quitFlag = True
                    break
                if move not in availableSpaces and move in theBoard.keys():
                    print("You can't enter a space that's already been taken. The options left are: " + str(availableSpaces))
                    move = input("Enter a valid move: ")
                elif move in theBoard.keys():
                    theBoard[move] = turn
                    break
                else:
                    print("You entered an invalid spot. The options left are these empty spaces: " + str(availableSpaces))
                    move = input("Enter a valid move: ")

            if quitFlag == True:
                break

            ## checkWin goes here and flags if a win occurs
            if checkWin(theBoard, turn):
                winFlag = True
                break

            availableSpaces.remove(move)

            if turn == 'X':
                turn = 'O'
            else:
                turn ='X'
            
            print('-' * 60)                             ## Line in between turns for aesthetic purposes
        
        print('-' * 60)
        print("End board: ")
        printBoard(theBoard)

    ## after print board say who wins with if, otherwise a tie message pops up
        if winFlag:
            print(turn + " won the game.")
        else:
            print("It was a tie.")
   
    else:
        break


print("Program ending...")



## Want to implement throw exceptions/check for valid keys  [DONE]

## Check if a win has been achieved after every move input              [DONE]
## Want to implement can't choose the same space                        [DONE]
## Want to implement a list that shows which spaces are left/open       [DONE]
## Want to prompt user to play again
## When available list is empty, print the end board, otherwise don't print the end board       [Scrapped to always print board]


## For available spaces left, we start with all spaces, and then remove ones with their values not  == ' '
## We need to implement this so it removes the move space after every input