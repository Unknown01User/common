from random import randint
field = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
def print_field(current_field):
    for row in field:
        for x in row:
            print(x, end=' ')
        print()
class Tank:
    def __init__(self, move_sells, shoot_sells, x, y):
        self.move_cells = move_sells
        self.shoot_cells = shoot_sells
        self.x = x
        self.y = y
        self.move_iter = 0
        self.shoot_iter = 0
        self.direction = None
        self.shoot_point_x = None
        self.shoot_point_y = None
        self.shoot_second_point_x = None
        self.shoot_second_point_y = None
        self.status = "game"
    def move_up(self):
        if self.y == 1:
            return 0
        else:
            self.y -= 1
            self.move_iter += 1
            return 1
    def move_down(self):
        if self.y == 10:
            return 0
        else:
            self.y += 1
            self.move_iter += 1
            return 1
    def move_left(self):
        if self.x == 1:
            return 0
        else:
            self.x -= 1
            self.move_iter += 1
            return 1
    def move_right(self):
        if self.x == 10:
            return 0
        else:
            self.x += 1
            self.move_iter += 1
            return 1
    def move_up_left(self):
        if self.x == 1 or self.y == 1:
            return 0
        else:
            self.x -= 1
            self.y -= 1
            self.move_iter += 1
            return 1
    def move_up_right(self):
        if self.x == 10 or self.y == 1:
            return 0
        else:
            self.x += 1
            self.y -= 1
            self.move_iter += 1
            return 1
    def move_down_left(self):
        if self.x == 1 or self.y == 10:
            return 0
        else:
            self.x -= 1
            self.y += 1
            self.move_iter += 1
            return 1
    def move_down_right(self):
        if self.x == 10 or self.y == 10:
            return 0
        else:
            self.x += 1
            self.y += 1
            self.move_iter += 1
            return 1
    def shoot(self):
        if self.shoot_cells == 1 and self.direction == "q":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x - 1
        elif self.shoot_cells == 1 and self.direction == "w":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x
        elif self.shoot_cells == 1 and self.direction == "e":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x + 1
        elif self.shoot_cells == 1 and self.direction == "a":
            self.shoot_point_y = self.y
            self.shoot_point_x = self.x - 1
        elif self.shoot_cells == 1 and self.direction == "s":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x
        elif self.shoot_cells == 1 and self.direction == "d":
            self.shoot_point_y = self.y
            self.shoot_point_x = self.x + 1
        elif self.shoot_cells == 1 and self.direction == "z":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x - 1
        elif self.shoot_cells == 1 and self.direction == "x":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x + 1
        elif self.shoot_cells == 2 and self.direction == "q":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x - 1
            self.shoot_second_point_y = self.y - 2
            self.shoot_second_point_x = self.x - 2
        elif self.shoot_cells == 2 and self.direction == "w":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x
            self.shoot_second_point_y = self.y - 2
            self.shoot_second_point_x = self.x
        elif self.shoot_cells == 2 and self.direction == "e":
            self.shoot_point_y = self.y - 1
            self.shoot_point_x = self.x + 1
            self.shoot_second_point_y = self.y - 2
            self.shoot_second_point_x = self.x + 2
        elif self.shoot_cells == 2 and self.direction == "a":
            self.shoot_point_y = self.y
            self.shoot_point_x = self.x - 1
            self.shoot_second_point_y = self.y
            self.shoot_second_point_x = self.x - 2
        elif self.shoot_cells == 2 and self.direction == "s":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x
            self.shoot_second_point_y = self.y + 2
            self.shoot_second_point_x = self.x
            field[tank.y + 1][tank.x] = "."
            field[tank.y + 2][tank.x] = "x"
        elif self.shoot_cells == 2 and self.direction == "d":
            self.shoot_point_y = self.y
            self.shoot_point_x = self.x + 1
            self.shoot_second_point_y = self.y
            self.shoot_second_point_x = self.x + 2
            field[tank.y][tank.x + 1] = "."
            field[tank.y][tank.x + 2] = "x"
        elif self.shoot_cells == 2 and self.direction == "z":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x - 1
            self.shoot_second_point_y = self.y + 2
            self.shoot_second_point_x = self.x - 2
        elif self.shoot_cells == 2 and self.direction == "x":
            self.shoot_point_y = self.y + 1
            self.shoot_point_x = self.x + 1
            self.shoot_second_point_y = self.y + 2
            self.shoot_second_point_x = self.x + 2
class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        if self.x == 1 and self.y == 1:
            random = randint(1, 3)
            if random == 1:
                self.x += 1
            elif random == 2:
                self.y += 1
            else:
                self.x += 1
                self.y += 1
        elif self.x == 10 and self.y == 1:
            random = randint(1, 3)
            if random == 1:
                self.x -= 1
            elif random == 2:
                self.y += 1
            else:
                self.x -= 1
                self.y += 1
        elif self.x == 1 and self.y == 10:
            random = randint(1, 3)
            if random == 1:
                self.x += 1
            elif random == 2:
                self.y -= 1
            else:
                self.x += 1
                self.y -= 1
        elif self.x == 10 and self.y == 10:
            random = randint(1, 3)
            if random == 1:
                self.x -= 1
            elif random == 2:
                self.y -= 1
            else:
                self.x -= 1
                self.y -= 1
        elif self.y == 1:
            random = randint(1, 5)
            if random == 1:
                self.x -= 1
            elif random == 2:
                self.x -= 1
                self.y += 1
            elif random == 3:
                self.y += 1
            elif random == 4:
                self.x += 1
                self.y += 1
            elif random == 5:
                self.x += 1
        elif self.y == 10:
            random = randint(1, 5)
            if random == 1:
                self.x -= 1
            elif random == 2:
                self.x -= 1
                self.y -= 1
            elif random == 3:
                self.y -= 1
            elif random == 4:
                self.x += 1
                self.y -= 1
            elif random == 5:
                self.x += 1
        elif self.x == 1:
            random = randint(1, 5)
            if random == 1:
                self.y -= 1
            elif random == 2:
                self.x += 1
                self.y -= 1
            elif random == 3:
                self.x += 1
            elif random == 4:
                self.x += 1
                self.y += 1
            elif random == 5:
                self.y += 1
        elif self.x == 10:
            random = randint(1, 5)
            if random == 1:
                self.y -= 1
            elif random == 2:
                self.x -= 1
                self.y -= 1
            elif random == 3:
                self.x -= 1
            elif random == 4:
                self.x -= 1
                self.y += 1
            elif random == 5:
                self.y += 1
        else:
            random = randint(1, 8)
            if random == 1:
                self.x -= 1
                self.y -= 1
            elif random == 2:
                self.y -= 1
            elif random == 3:
                self.x += 1
                self.y -= 1
            elif random == 4:
                self.x += 1
            elif random == 5:
                self.x += 1
                self.y += 1
            elif random == 6:
                self.y += 1
            elif random == 7:
                self.y += 1
                self.x -= 1
            elif random == 8:
                self.x -= 1
print("Menu:\n"
      "\n"
      "choose tank\n"
      "1 - Tank can move by 2 cells and shoot by 1 cell \n"
      "2 - Tank can move by 1 cell and shoot by 2 cells \n")
tank_type = int(input())
random_x = randint(1, 10)
random_y = randint(1, 10)
tank = Tank(0, 0, random_x, random_y)
if tank_type == 1:
    tank = Tank(2, 1, random_x, random_y)
    field[random_y][random_x] = "T"
elif tank_type == 2:
    tank = Tank(1, 2, random_x, random_y)
    field[random_y][random_x] = "T"
else:
    print("this type of tank is not found")
while abs(random_x - tank.x) <= tank.shoot_cells and abs(random_y - tank.y) <= tank.shoot_cells:
    random_x = randint(1, 10)
    random_y = randint(1, 10)
    target = Target(random_x, random_y)
field[target.y][target.x] = "@"
print_field(field)
while tank.status == "game":
    print("your turn")
    while tank.move_iter < tank.move_cells or tank.shoot_iter < 1:
        direction = input()
        field[tank.y][tank.x] = " "
        tank_old_x = tank.x
        tank_old_y = tank.y
        if direction == "q" and tank.move_iter < tank.move_cells:
            tank.direction = "q"
            tank.move_up_left()
        elif direction == "w" and tank.move_iter < tank.move_cells:
            tank.direction = "w"
            tank.move_up()
        elif direction == "e" and tank.move_iter < tank.move_cells:
            tank.direction = "e"
            tank.move_up_right()
        elif direction == "a" and tank.move_iter < tank.move_cells:
            tank.direction = "a"
            tank.move_left()
        elif direction == "s" and tank.move_iter < tank.move_cells:
            tank.direction = "s"
            tank.move_down()
        elif direction == "d" and tank.move_iter < tank.move_cells:
            tank.direction = "d"
            tank.move_right()
        elif direction == "z" and tank.move_iter < tank.move_cells:
            tank.direction = "z"
            tank.move_down_left()
        elif direction == "x" and tank.move_iter < tank.move_cells:
            tank.direction = "x"
            tank.move_down_right()
        elif direction == " " and tank.shoot_iter < 1:
            tank.shoot_iter += 1
            tank.shoot()
            if tank.shoot_cells == 1:
                if not field[tank.shoot_point_y][tank.shoot_point_x] == "#":
                    field[tank.shoot_point_y][tank.shoot_point_x] = "x"
                    if tank.shoot_point_x == target.x and tank.shoot_point_y == target.y:
                        tank.status = "win"
                        print("you win!")
                        exit(0)
            elif tank.shoot_cells == 2:
                if not field[tank.shoot_point_y][tank.shoot_point_x] == "#":
                    if field[tank.shoot_point_y][tank.shoot_point_x] == "@":
                        field[tank.shoot_point_y][tank.shoot_point_x] = "@"
                    else:
                        field[tank.shoot_point_y][tank.shoot_point_x] = "."
                    if not field[tank.shoot_second_point_y][tank.shoot_second_point_x] == "#":
                        field[tank.shoot_second_point_y][tank.shoot_second_point_x] = "x"
                        if tank.shoot_second_point_x == target.x and tank.shoot_second_point_y == target.y:
                            tank.status = "win"
                            print("you win!")
                            exit(0)
                    else:
                        field[tank.shoot_point_y][tank.shoot_point_x] = "x"
                        if tank.shoot_point_x == target.x and tank.shoot_point_y == target.y:
                            tank.status = "win"
                            print("you win!")
                            exit(0)
        elif tank.move_iter == tank.move_cells and tank.shoot_iter < 1:
            print("you can't move anymore")
            continue
        else:
            print("command not found")
        if tank.x == target.x and tank.y == target.y:
            tank.move_iter -= 1
            tank.x = tank_old_x
            tank.y = tank_old_y
            continue
        else:
            field[tank.y][tank.x] = "T"
            print_field(field)
    tank.move_iter = 0
    tank.shoot_iter = 0
    print("computer's turn")
    field[target.y][target.x] = " "
    field[tank.shoot_point_y][tank.shoot_point_x] = " "
    if tank.shoot_cells == 2:
        field[tank.shoot_second_point_y][tank.shoot_second_point_x] = " "
    target_old_x = target.x
    target_old_y = target.y
    target.move()
    if target.x == tank.x and target.y == tank.y:
        target.x = target_old_x
        target.y = target_old_y
        target.move()
    field[target.y][target.x] = "@"
    print_field(field)
