import datetime
class Person:
    def __init__(self,name,country,DOB):
        self.name=name
        self.country=country
        self.DOB=DOB
    def calcage(self):
        current_year=datetime.datetime.now().year
        yob=int(self.DOB.split("-")[2])
        age=current_year-yob
        return age

omyma=Person("omyma","cairo","13-12-1994") 
print(omyma.calcage())