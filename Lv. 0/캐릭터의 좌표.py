def solution(keyinput, board):
    x, y = 0, 0
    x_limit, y_limit = board[0]//2, board[1]//2

    move = {"left": (-1, 0), "right": (1, 0), "up": (0,1), "down": (0, -1)}

    for k in keyinput:
        dx, dy = move[k]
        x += dx
        y += dy

        if x > x_limit:
            x = x_limit
        elif x < -x_limit:
            x = -x_limit

        if y > y_limit:
            y = y_limit
        elif y < -y_limit:
            y = -y_limit

    return [x, y]

# print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["right", "right", "right", "right", "right", "left"], [9, 5])) #[3,0]