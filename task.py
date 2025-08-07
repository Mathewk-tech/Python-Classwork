class Human():
    def __init__(self,gender,name):
        print("The initializer was called")
        print(name)
        print(gender)

    def another_one(self):
            print("This is another method")


adam=Human(name="Mathew",gender="male")
adam.another_one()