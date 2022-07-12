BOARD_LAYOUT_0 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class SnakeGame:
    def __init__(self, board_size, tick_speed, board_state=None):
        self.board_size = board_size
        self.tick_speed = tick_speed

        if not board_state:
            self.board = [[0] * board_size[0]] * board_size[1]  # 0: Empty / 1: Wall / 2: Snake
        else:
            self.board = board_state
            self.board_size = (len(board_state[0]), len(board_state))
        
        # Calculate start size
    
    def reset(self):
        self.board = [[0] * self.board_size[0]] * self.board_size[1]

    def display(self):
        for y in range(self.board_size[1]):
            line = ""
            for x in range(self.board_size[0]):
                if self.board[y][x] == 0:
                    line += "'"
                elif self.board[y][x] == 1:
                    line += "#"
                elif self.board[y][x] == 2:
                    line += "*"
            print(line)

    # Handle game step -> Logic, graphics
    def step(self):
        self.display()