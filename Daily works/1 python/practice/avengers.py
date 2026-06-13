
# super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# class avengers:
#     def__init___(self,name, age,gender,super_power,weapon):
#     self.name = name 
#     self.age = age 
#     self.gender = gender
#     self.super_power = super_power
#     sel.weapon = weapon





class BMW:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car ...")

    def stop(self):
        print("Stopping the car ...")

    def drive(self):
        pass


class ThreeClass(BMW):
    def __init__(self, CuriseAssistEnabled, name, model, year):
        BMW.__init__(self, name, model, year)
        self.CuriseAssistEnabled = CuriseAssistEnabled

    def display(self):
        print(self.CuriseAssistEnabled)

    def drive(self):
        print("Three Class is being driven..")


threeClass = ThreeClass(True, "BMW", "328i", 2018)
threeClass.start()
threeClass.drive()
threeClass.stop()