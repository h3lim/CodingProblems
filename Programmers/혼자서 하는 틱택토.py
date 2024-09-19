def solution(board):
    def check_bingo(board):
        # Check horizontal and vertical lines
        for i in range(3):
            if all(board[i][j] == board[i][0] and board[i][0] != 0 for j in range(3)):
                return True
            if all(board[j][i] == board[0][i] and board[0][i] != 0 for j in range(3)):
                return True

        # Check diagonal lines
        if all(board[i][i] == board[0][0] and board[0][0] != 0 for i in range(3)):
            return True
        if all(board[i][2 - i] == board[0][2] and board[0][2] != 0 for i in range(3)):
            return True

        return False

    cnt = 0
    newBoardO = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
    newBoardX = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
    boardO, boardX = [0] * 9, [0] * 9
    cntO, cntX = 0, 0
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                boardO[cnt] = 1
                newBoardO[i][j] = 1
                cntO += 1
            elif board[i][j] == 'X':
                boardX[cnt] = 1
                newBoardX[i][j] = 1
                cntX += 1
            cnt += 1
    if cntO > 2 and check_bingo(newBoardO) == True:
        if cntX >= cntO:
            return 0
    if cntX > 2 and check_bingo(newBoardX) == True:
        if cntX < cntO:
            return 0
    cnt = 0
    while 1:
        if cnt % 2 == 0 and 1 in boardO:
            o = boardO.index(1)
            boardO[o] = 2
        elif cnt % 2 == 0 and 1 not in boardO and 1 in boardX:

            return 0

        if cnt % 2 == 1 and 1 in boardX:
            x = boardX.index(1)
            boardX[x] = 2
        elif cnt % 2 == 1 and 1 not in boardX and 1 in boardO:

            return 0

        if 1 not in boardO and 1 not in boardX:
            break
        cnt += 1
    return 1

#1. O가 빙고가 되는 상황에 X의 갯수가 O의 갯수와 같거나 많은 상황

#2. X가 빙고가 되는 상황에 O의 갯수가 O의 갯수와 많은 상황

#3. O가 선공이기에 홀수번째 상황에 O는 더 이상 없고 X만 있는 상황

#4. 짝수번째 상황에 X는 없고 O만 남아있는 상황