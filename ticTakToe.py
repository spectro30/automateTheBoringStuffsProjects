board = { 'top-L':' ', 'top-M':' ','top-R':' ','mid-L':' ','mid-M':' ',
             'mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printBoard():
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard()

turn = 'X'
for i in range(9):
    print('Turn for ' + turn + '. Choose Position')
    while(True):
        move = input()
        if(board[move] == ' '):    
            board[move] = turn
            break
        print('Cell already booked')
    if turn == 'X':
        turn = 'O'
    else :
        turn = 'X'
    printBoard()
