class Human():
    def __init__(self,gender,name):
        print("The initializer was called")
        self.gender=gender
        self.name=name
        
        if self.gender=="male":
          self.ribs=23
        else:
             self.ribs=24
       

    def another_one(self,gender,name):
            print("This is another method")
            self.gender=gender
            self.name=name


adam=Human(name="Mathew",gender="male")
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)

adam.another_one(name="Grace",gender="female")
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)
