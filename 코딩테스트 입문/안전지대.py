import copy

def solution(board):
    bomb = copy.deepcopy(board)
    b_len = len(board)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (1, -1), (1, 1), (-1, 1)]

    for row_idx in range(b_len):
        for col_idx in range(b_len):
            if bomb[row_idx][col_idx] == 1:
                for dx, dy in directions:
                    nx, ny = row_idx + dx, col_idx + dy

                    if 0 <= nx < b_len and 0 <= ny < b_len:
                        bomb[nx][ny] += 1
    
    cnt = 0
    for i in range(b_len):
        for j in range(b_len):
            if bomb[i][j] == 0:
                cnt += 1
    return cnt



print(solution([[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 0, 0]])) #16

print(solution([[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0], 
                [0, 0, 0, 0, 0]])) #13

print(solution([[1, 1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1, 1]])) #0