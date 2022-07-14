import os
import random
import time
#from pynput import keyboard # https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

MAP_0 = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
]

# UTILS
def clear_trm():
    os.system("cls" if os.name == "nt" else "clear")

##  Exceptions Sinnvoll für Sprünge in Spiel Logik
# Wenn Schlange Wand berührt, oder sich selbst isst
class GameOver(Exception):
    def __init__(self, score):
        self.score = score

# A snake game one can play inside the console
class SnakeGame:
    def __init__(self, step_speed, score_multiplyer=1, fruit_spawn_delay=20,map_state=None, map_size=(10, 10)):
        self.score_multiplyer = score_multiplyer
        self.fruit_spawn_delay = fruit_spawn_delay
        self.initial_map_state = map_state
        self.step_speed = step_speed
        self.curr_step = 0
        self.curr_score = 0
        self.snake_last_dir = "U"
        self.snake_body = [(3, 3)] # TODO: Generate!
        self.fruit_pos = (5, 5)

        if not map_state:
            self.map = [[0] * map_size[0]] * map_size[1]  # 0: Empty / 1: Wall / 2: Snake
        else:
            self.map = map_state
            self.map_size = (len(map_state[0]), len(map_state))
        
        # Tastenanschläge
        #self.listener = keyboard.Listener(
        #    on_press=self.on_input)
        #self.listener.start()
    
    # Setzt Spile zurück
    def reset(self):
        self.curr_step = 0
        if self.initial_map_state:
            self.map = self.initial_map_state
        else:
            self.map = [[0] * self.map_size[0]] * self.map_size[1]

    def display(self):
        print("Schritt {}".format(self.curr_step))
        print("Punkte: {}".format(self.curr_score))
        for y in range(self.map_size[1]):
            line = ""
            for x in range(self.map_size[0]):
                s = False
                # Snake
                for e in self.snake_body:
                    if e == (x, y):
                        line += "*"
                        s = True
                # Map
                if not s:
                    if self.map[y][x] == 0:
                        line += " "
                    elif self.map[y][x] == 1:
                        line += "#"
                # Fruit
                if self.fruit_pos == (x, y):
                    line = line[:-1]
                    line += "+"
            print(line)

    def get_snake_head(self):
        return self.snake_body[0]
    
    def spawn_fruit(self):
        self.fruit_pos = (random.randint(0,self.map_size[0] -1), random.randint(0, self.map_size[1] - 1))
        if self.map[self.fruit_pos[1]][self.fruit_pos[0]] == 1:
            self.spawn_fruit()
    
    def on_input(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            pass

    # Bewegt schlange ein Feld in Richtung (U, D, L, R) -> +1 Länge wenn eat=True
    def move_snake(self, dir=None):
        dir = input("Dir: ")
        if dir == "U" and self.snake_last_dir == "D":
            dir = self.snake_last_dir
        elif dir == "D" and self.snake_last_dir == "U":
            dir = self.snake_last_dir
        elif dir == "L" and self.snake_last_dir == "R":
            dir = self.snake_last_dir
        elif dir == "R" and self.snake_last_dir == "L":
            dir = self.snake_last_dir
        if not dir: dir = self.snake_last_dir
        if len(self.snake_body) <= 0: return
        if not dir:
            dir = self.snake_last_dir
        self.snake_last_dir = dir
        head = self.snake_body[0]
        if dir == "U":
            head = (head[0], head[1] - 1)
        elif dir == "D":
            head = (head[0], head[1] + 1)
        elif dir == "L":
            head = (head[0] - 1, head[1])
        elif dir == "R":
            head = (head[0] + 1, head[1])
        
        # Seitensprung
        if head[0] < 0:
            head = (self.map_size[0] - 1, head[1])
        elif head[0] >= self.map_size[0]:
            head = (0, head[1])
        if head[1] < 0:
            head = (head[0], self.map_size[1] - 1)
        elif head[1] >= self.map_size[1]:
            head = (head[0], 0)
        
        self.snake_body.insert(0, head)
        if head != self.fruit_pos:
            del self.snake_body[-1]
        else:
            self.curr_score += 1 * self.score_multiplyer
            self.spawn_fruit()

    # Bricht ab wenn Spiel vorbei ist
    def check_state(self):
        # Schlange isst sich selbst
        head = self.get_snake_head()
        if len(self.snake_body) > 0:
            for e in self.snake_body[1:]:
                if head == e:
                    raise GameOver(self.curr_score)
        # Schlange ist auf Wand
        if self.map[head[1]][head[0]] == 1:
            raise GameOver(self.curr_score)

    # Handle game step -> Logic, graphics
    def step(self):
        self.curr_step = self.curr_step + 1
        #clear_trm()
        print("\n\n\n===========")
        self.check_state()

        # Spawn
        if self.curr_step % self.fruit_spawn_delay == 0:
            self.spawn_fruit()
        #if self.curr_step

        self.move_snake()
        self.display()
    
    def game_loop(self):
        self.step()
        time.sleep(1 / self.step_speed)