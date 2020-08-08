import random
import keyboard

class Pos:
    x=0
    y=0
class Tank:
    pos=Pos()
    shoot_range=1
    movements_per_turn=1
    direction='W'
    def set_pos(self,x:int,y:int):
        self.pos.x=x
        self.pos.y=y
class FastTank(Tank):
    movements_per_turn = 2
class LongRangedTank(Tank):
    shoot_range = 2
class Map:
    border_symbol='#'
    size_of_field=10
    field=None
    def set_border_line(self,field):
        line=[]
        field.append(line)
        for i in range(self.size_of_field):
            line.append(self.border_symbol)
    def set_tank_on_map(self,tank:Tank,icon):
        self.field[tank.pos.y][tank.pos.x]=icon
    def set_map(self,hero : Tank,enemy : Tank,removeShots:bool):
        if(self.field is None):
            self.field=[]
            self.set_border_line(self.field)
            for y in range(self.size_of_field-2):
                line=[]
                self.field.append(line)
                line.append(self.border_symbol)
                for x in range(1,self.size_of_field-1):
                    line.append(' ')
                line.append(self.border_symbol)
            self.set_border_line(self.field)
        else:
            for y in range(len(self.field)):
                for x in range(len(self.field[y])):
                    if self.field[y][x]=='T' or self.field[y][x]=='@' or (removeShots and self.field[y][x]=='.'):
                        self.field[y][x]=' '
        self.set_tank_on_map(hero,'T')
        self.set_tank_on_map(enemy,'@')
    def print_map(self):
        for line in self.field:
            print(''.join(line))

class Menu:
    @classmethod
    def show(cls):
        print("Choose tank type \n  -1 - help\n  1 - 2x speed 1 - shot range \n  2 - 1x speed 2 - shot range")
    @classmethod
    def choose_tank(cls):
        tank_type=int(input())
        if (tank_type==1):
            return FastTank()
        if(tank_type==2):
            return LongRangedTank()
    @classmethod
    def get_tank_class(cls):
        dict={1,FastTank,2,LongRangedTank}
        return dict(int(input()))
class Battle:
    actions_list=['A','W','S','D',' ']
    @classmethod
    def help(cls):
        print("AWSD - move, space - shoot")
    @classmethod
    def generate_random_pos(cls):
        pos = Pos()
        pos.x=random.randint(1,Map.size_of_field-2)
        pos.y=random.randint(1,Map.size_of_field-2)
        return pos
    @classmethod
    def set_shell_trace(cls,map:Map,x:int,y:int):
        if(map.field[y][x]==' '):
            map.field[y][x]='.'
        if(map.field[y][x]=='@'):
            map.field[y][x]='X'
    @classmethod
    def player_turn(cls,tank:Tank,command,map:Map):
        if(command=='W'):
            if(tank.pos.y>1):
                tank.pos.y-=1
                tank.direction='W'
                return 0
            else:
                return -2
        if(command=='S'):
            if(tank.pos.y<map.size_of_field-2):
                tank.pos.y+=1
                tank.direction='S'
                return 0
            else:
                return -2
        if(command=='A'):
            if(tank.pos.x>1):
                tank.pos.x-=1
                tank.direction='A'
                return 0
            else:
                return -2
        if(command=='D'):
            if(tank.pos.x<map.size_of_field-2):
                tank.pos.x+=1
                tank.direction='D'
                return 0
            else:
                return -2
        if(command==' '):
            if(tank.direction=='W'):
                for i in range(1,tank.shoot_range+1):
                    trace_point=tank.pos.y-i
                    if(trace_point>1):
                        cls.set_shell_trace(map,tank.pos.x,trace_point)
            if(tank.direction=='S'):
                for i in range(1,tank.shoot_range+1):
                    trace_point=tank.pos.y+i
                    if(trace_point<map.size_of_field-1):
                        cls.set_shell_trace(map,tank.pos.x,trace_point)
            if(tank.direction=='D'):
                for i in range(1,tank.shoot_range+1):
                    trace_point=tank.pos.x+i
                    if(trace_point<map.size_of_field-1):
                        cls.set_shell_trace(map,trace_point,tank.pos.y)
            if(tank.direction=='A'):
                for i in range(1,tank.shoot_range+1):
                    trace_point=tank.pos.x-i
                    if(trace_point):
                        cls.set_shell_trace(map,trace_point,tank.pos.y)
            return 0
        cls.help()
        return -1
    @classmethod
    def start(cls,player):
        battle_map=Map()
        player.pos=cls.generate_random_pos()
        enemy=Tank()
        enemy.pos=player.pos
        while abs(enemy.pos.x-player.pos.x)<=player.shoot_range or abs(enemy.pos.y-player.pos.y)<=player.shoot_range:
            enemy.pos=cls.generate_random_pos()
        battle_map.set_map(player,enemy,False)
        while True:
            battle_map.set_map(player,enemy,True)
            for i in range(player.movements_per_turn):
                return_value=1
                while return_value!=0:
                    return_value=cls.player_turn(player,input("Enter command : "),battle_map)
                    if(battle_map.field[enemy.pos.y][enemy.pos.x]=='X'):
                        battle_map.print_map()
                        print("You won")
                        return 0
                    if(return_value==-2):
                        print("There is a wall.I can't do that")
                battle_map.set_map(player,enemy,False)
                battle_map.print_map()
            return_value=1
            while return_value!=0:
                return_value=cls.player_turn(enemy,cls.actions_list[random.randint(0,len(cls.actions_list)-2)],battle_map)
            battle_map.set_map(player,enemy,False)
            battle_map.print_map()
class Game:
    @classmethod
    def start(cls):
        Menu.show()
        Battle.start(Menu.choose_tank())
Game.start()
