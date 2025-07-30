class Animals:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.health=50
        self.happiness=50
    def display_info(self):
        print(f"name:{self.name},age:{self.age},health:{self.health},happiness:{self.happiness}")
    def feed(self):
        self.health+=10
        self.happiness+=10
class Lion(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.roar_power = 100
    def feed(self):
        self.health +=15
        self.happiness += 5
class Monkey(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.banana_count=0
    def feed(self):
        self.banana_count +=1
        self.health +=5
        self.happiness+= 15
class Bear(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.hibernate_ready = False
    def feed(self):
        self.health += 12
        self.happiness +=8
        if self.health > 80 :
            self.hibernate_ready= True
            print("The bear is now ready to hibernate ")
class Tiger(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.speed = 90
    def feed(self):
        self.health += 10
        self.happiness +=10
class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name =zoo_name
    def add_lion(self,name):
        self.animals.append(Lion(name,5))
    def add_tiger(self,name):
        self.animals.append(Tiger(name,3))
    def print_all_info(self):
        print("-"*30,self.name,"-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1=Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("shere khan")
zoo1.print_all_info()