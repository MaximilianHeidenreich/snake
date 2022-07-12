from game import SnakeGame, BOARD_LAYOUT_0

if __name__ == "__main__":
    game = SnakeGame((10, 10), 1, BOARD_LAYOUT_0)
    game.step()