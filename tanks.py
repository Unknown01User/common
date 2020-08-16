import random
import math

class Game:
    TURNS = {'Q': (-1, -1),
             'W': (-1, 0),
             'E': (-1, 1),
             'A': (0, -1),
             'Z': (1, -1),
             'X': (1, 0),
             'D': (0, 1),
             'C': (1, 1)}

    def __init__(self):
        self.pf = None
        self.tank = None
        self.target = None
        self.last_direction = self.TURNS['W']
        self._is_game_over = False

    def start(self):
        self._start_game()

    def _start_game(self):
        while True:
            self.pf = PlayingField()
            self.pf.create_playing_field()
            self.pf.print_playing_field()
            if not self._choose_tank():
                print("Game is finished!")
                break
            self._put_tank()
            self._put_target()
            self.pf.print_playing_field()
            while not self._is_game_over:
                self._make_turn()
                self._move_target()

    def _choose_tank(self):
        print("Please enter 1 to choose 1 type of tank which move for 2 distances and shoot for 1 distances"
              "or enter 2 to choose 2 type of tank to which move for 1 distances and shoot for 2 distances."
              "If you want to finish, please, press 3")
        while True:
            type_of_tank = input()
            if type_of_tank == '1':
                self.tank = Tank(2, 1)
                return True
            if type_of_tank == '2':
                self.tank = Tank(1, 2)
                return True
            if type_of_tank == '3':
               return False
            else:
                print("Invalid input! Try again!")


    def _put_tank(self):
        x = random.randint(0, self.pf.FIELD_SIZE_HEIGHT - 1)
        y = random.randint(0, self.pf.FIELD_SIZE_LENGTH - 1)
        self.tank.set_position(x, y)
        self.pf.put_game_object(self.tank)

    def _put_target(self):
        self.target = Target()
        while True:
            x = random.randint(0, self.pf.FIELD_SIZE_HEIGHT - 1)
            y = random.randint(0, self.pf.FIELD_SIZE_LENGTH - 1)
            x1, y1 = self.tank.get_position()
            if abs(x - x1) > self.tank.shoot_distance or abs(y - y1) > self.tank.shoot_distance:
                self.target.set_position(x, y)
                self.pf.put_game_object(self.target)
                break

    def _make_turn(self):
        is_shoot_allowed = True
        print("Please, choose your turn")
        print("Allowed actions: for moves: {},  and for shooting: ' '".format(list(self.TURNS.keys())))
        step_count = self.tank.step_distance
        while step_count > 0 and not self._is_game_over:
            while True:
                choice = input()
                choice = choice.upper()
                print("Choice '{}', is_shoot_allowed = {}".format(choice, is_shoot_allowed))
                if choice == " " and is_shoot_allowed:
                    step_count = 0
                    self._make_shoot()
                    break
                if choice not in self.TURNS:
                    print("Invalid input! Try again!")
                    continue
                turn = self.TURNS[choice]
                if self.pf.is_move_allowed(self.tank, turn):
                    self.pf.move_game_object(self.tank, turn)
                    self.last_direction = turn
                    self.pf.print_playing_field()
                    is_shoot_allowed = False
                    break
                else:
                    print("Such turn isn`t allowed!")
            step_count -= 1

    def _move_target(self):
        while True and not self._is_game_over:
            direction = random.choice(list(self.TURNS))
            if self.pf.is_move_allowed(self.target, self.TURNS[direction]):
                self.pf.move_game_object(self.target, self.TURNS[direction])
                break
        self.pf.print_playing_field()

    def _make_shoot(self):
        shell_position = self.pf.get_new_position(self.tank, self.last_direction)
        shell = Shell()
        shell.set_position(shell_position[0], shell_position[1])
        shoot_distance = self.tank.shoot_distance

        while shoot_distance:
            if self.target.get_position() == shell.get_position():
                shell.symbol = 'X'
                self.pf.put_game_object(shell)
                self._is_game_over = True
                print("YOU HAVE WON!")
                return
            elif self.pf.is_move_allowed(shell, (0, 0)):
                self.pf.put_game_object(shell)
                self.pf.print_playing_field()
            else:
                return
            self.pf.remove_game_object(shell)
            shoot_distance -= 1
            if shoot_distance != 0:
                new_x, new_y = self.pf.get_new_position(shell, self.last_direction)
                shell.set_position(new_x, new_y)

        self.pf.print_playing_field()
        print("Miss! Distance is {:.2f}".format(shell.get_distance(self.target)))


class PlayingField:
    FIELD_SIZE_HEIGHT = 10
    FIELD_SIZE_LENGTH = 10
    EMPTY_CELL = " "

    def __init__(self):
        self.playing_field = []

    def create_playing_field(self):
        for index in range(self.FIELD_SIZE_HEIGHT):
            field_length = []
            for index1 in range(self.FIELD_SIZE_LENGTH):
                field_length.append(self.EMPTY_CELL)
            self.playing_field.append(field_length)

    def print_playing_field(self):
        print("#" * (self.FIELD_SIZE_LENGTH + 2))
        for row in self.playing_field:
            line = "".join(row)
            print(f"#{line}#")

        print("#" * (self.FIELD_SIZE_LENGTH + 2))

    def put_game_object(self, game_object):
        x, y = game_object.get_position()
        self.playing_field[x][y] = game_object.symbol

    def remove_game_object(self, game_object):
        x, y = game_object.get_position()
        self.playing_field[x][y] = self.EMPTY_CELL

    def get_new_position(self, game_object, turn):
        x, y = game_object.get_position()
        to_x, to_y = turn
        return x + to_x, y + to_y

    def is_move_allowed(self, game_object, turn):
        new_x, new_y = self.get_new_position(game_object, turn)
        if new_x < 0 or new_x >= self.FIELD_SIZE_HEIGHT or new_y < 0 or new_y >= self.FIELD_SIZE_LENGTH:
            return False
        if self.playing_field[new_x][new_y] != self.EMPTY_CELL:
            return False
        return True

    def move_game_object(self, game_object, turn):
        x, y = game_object.get_position()
        new_x, new_y = self.get_new_position(game_object, turn)
        self.playing_field[x][y] = self.EMPTY_CELL
        game_object.set_position(new_x, new_y)
        self.playing_field[new_x][new_y] = game_object.symbol


class GameObject:
    def __init__(self, symbol):
        self.symbol = symbol
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_distance(self, game_object):
        return math.sqrt(math.pow(self.x - game_object.x, 2) + math.pow(self.y - game_object.y, 2))


class Tank(GameObject):
    def __init__(self, step_distance, shoot_distance):
        super(Tank, self).__init__('T')
        self.step_distance = step_distance
        self.shoot_distance = shoot_distance


class Target(GameObject):
    def __init__(self):
        super(Target, self).__init__('@')


class Shell(GameObject):
    def __init__(self):
        super(Shell, self).__init__('.')


g = Game()
g.start()
