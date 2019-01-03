from operator import itemgetter


def isPlayerWon(board, champ):

    if (board[0] == champ and board[1] == champ and board[2] == champ or
        board[3] == champ and board[4] == champ and board[5] == champ or
        board[6] == champ and board[7] == champ and board[8] == champ or
        board[0] == champ and board[3] == champ and board[6] == champ or
        board[1] == champ and board[4] == champ and board[7] == champ or
        board[2] == champ and board[5] == champ and board[8] == champ or
        board[0] == champ and board[4] == champ and board[8] == champ or
        board[2] == champ and board[4] == champ and board[6] == champ):
        return True
    else:
        return False


def avail(board):
    return [int(i) for i in board if (i != 'X' and i != 'O')] 

def minmax(board, champ):
    availablePlaces = avail(board)
    
    if isPlayerWon(board, 'X'):
        return 0, -100
    elif isPlayerWon(board, 'O'):
        return 0, 100
    elif availablePlaces == []:
        return 0, 0

    validMoves = []

    for i in availablePlaces:
        board[i] = champ

        if champ == 'O':
            score = minmax(board, 'X')[1]
            validMoves.append((i, score))
        elif champ == 'X':
            score = minmax(board, 'O')[1]
            validMoves.append((i, score))

        board[i] = i

    if champ == 'X':
        return min(validMoves, key=itemgetter(1))
    elif champ == 'O':
        return max(validMoves, key=itemgetter(1))



def drawBoard(board):

    # for i in range(3):
    #     print(board[3*i : 3*i+3])

    for i in range(3):
        for j in range(3):
            if board[i*3 + j] != 'X' and board[i*3 + j] != 'O':
                print(' ', end=' | ')
            else:
                print(board[i*3 + j], end=' | ')
        else:
            print()
        print('-' * 11)
            


def main():

    board = [str(i) for i in range(9)]
    # print(board)

    human = 'X'
    bot = 'O'
    drawBoard(board)
    while True:

        
        # print(board)
        humanMove = int(input('Enter the position: '))
        
        if((humanMove < 0 or humanMove > 8) or 
            board[humanMove] == 'X' or 
            board[humanMove] == 'O'):
            
            print('Invalid Move!! Try again!!')
            continue

        board[humanMove] = human

        botMove = minmax(board, bot)[0]
        print(botMove)
        board[botMove] = bot

        drawBoard(board)
        if isPlayerWon(board, 'X'):
            print('You Won')
            break
        elif isPlayerWon(board, 'O'):
            print('You Lose')
            break
        elif avail(board) == []:
            print('Tied')
            break


if __name__ == '__main__':
    main()
