class Shape:
    def __init__(self,name):
        self.name=name

    def describe(self):
        """describing the shape"""
        print(f"This shape is called {self.name}")  
    def area(self):
        print(f"The area of {self.name} is x")
# shape1=Shape(name="Circle")  
# shape1.describe()


class rectangle(Shape):
    def __init__(self, length,width):
        super().__init__("rectangle")
        self.length=length
        self.width=width

    def area(self):
        a=self.length*self.width
        print(f"For area of shape {self.name},the area is {a}")
       

r1=rectangle(10,3)  
r1.describe()  
r1.area() 
print("The shape is:",r1.name)


class circle(Shape):
    def __init__(self,radius):
        super().__init__("rectangle")
        self.radius=radius
       

    def area(self):
        a=3.142*self.radius
        print(f"For area of shape {self.name},the area is {a}")

c1=circle(10)
c1.describe()
c1.area()        