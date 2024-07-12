# box = ((x_start, x_end), (y_start, y_end))
boxes = [[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],

         [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],

         [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],

         [(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)],

         [(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5), (5, 5)],

         [(6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5)],

         [(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8)],

         [(3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (3, 8), (4, 8), (5, 8)],

         [(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8)]]


def solver(board):
    coord = [10, 10]
    for j in range(9):
        for i in range(9):
            if board[j][i] == '.':
                coord[0] = i
                coord[1] = j
                break
        else:
            continue
        break

    if coord == [10, 10]:
        return True

    col = [board[i][coord[0]] for i in list(range(9))]
    row = [board[coord[1]][i] for i in list(range(9))]
    square = []

    for b in boxes:
        if (coord[0], coord[1]) in b:
            for i in b:
                square.append(board[i[1]][i[0]])
            break

    for num in range(1, 10):
        num = str(num)
        if num not in col and num not in row:
            if num not in square:
                board[coord[1]][coord[0]] = num
                if solver(board):
                    return True
                board[coord[1]][coord[0]] = '.'
    return False


def return_solution(board):
    solver(board)
    return board

