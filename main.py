from game import SnakeGame, GameOver, MAP_0
import sys

if __name__ == "__main__":
    while True:
        try:
            # Schwierigkeit
            schwierigkeit = 0
            while True:
                print("Schwierigkeitsstufen:")
                print("1: Einfach (Punkte x1)")
                print("2: Mittel  (Punkte x2)")
                print("3: Schwer  (Punkte x3)")
                d = input("Wähle eine Schwierigkeitsstufe (1-3):")
                try:
                    d = int(d)
                    if d >= 1 and d <= 3:
                        schwierigkeit = d
                        break
                except:
                    pass
                print("Bitte gib eine valide Zahl zwischen 1 und 3 an!")

            speed = 1
            m = 1
            if schwierigkeit == 1:
                speed = 1
                m = 1
            elif schwierigkeit == 2:
                speed = 4
                m = 2
            elif schwierigkeit == 3:
                speed = 7
                m = 3

            game = SnakeGame(speed, score_multiplyer=m, map_state=MAP_0)
            # game = SnakeGame(speed, score_multiplyer=m, map_size=(20, 11))
            
            # game.game_loop()
            while True:
                game.step()
        except GameOver as e:
            print("GameOver! Punkte: {}".format(e.score))
            print("Ein neues Spiel wird automatisch gestartet!")
            i = input("Gib 'n' ein, um kein neues Spiel zu starten und das Programm zu beenden: ")
            if i.lower() == "n":
                sys.exit(0)