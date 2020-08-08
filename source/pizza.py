import time
class Pizza:
    first_steps=[(1,"Making dough"),(1,"Making souce")]
    special_steps=[(1,"Putting ingredients")]
    last_steps=[(1,"Warming"),(1,"Splitting"),(1,"Pizza is ready")]
    def preapare_steps(self,*steps):
        for step_arr in steps:
            for i in step_arr:
                print(i[1])
                time.sleep(i[0])
    def __init__(self):
        self.preapare_steps(self.first_steps,self.special_steps,self.last_steps)
class Pizza_Mushrooms(Pizza):
    special_steps = [(1,"Putting birches")]
    def __init__(self):
        super().__init__()
class Pizza_Meat(Pizza):
    special_steps = [(1,"Putting meat"),(1,"Putting bacon")]
    def __init__(self):
        super().__init__()
class Pizza_Vegetables(Pizza):
    special_steps = [(1,"Putting cheese"),(1,"Putting tomatoes")]
    def __init__(self):
        super().__init__()
pizzaType=int(input("Enter pizza type number\n 1 - mushrooms \n 2 - vegetables \n 3 - meat"))
constuctors={1:Pizza_Mushrooms,2:Pizza_Meat,3:Pizza_Vegetables}
pizza=constuctors[pizzaType]()
print(type(pizza))

