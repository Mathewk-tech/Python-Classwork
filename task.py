from datetime import datetime
def write_file(f_name,txt):
         with open(f_name,"a") as f:
          f.write(txt+"\n")

class Human():
    
    def __init__(self,gender,name):
        print("The initializer was called")
        self._gender=gender
        self._name=name
        
        if self._gender=="male":
          self._ribs=23
        else:
             self._ribs=24


    @property
    def name(self):
         print("Somebody is try to get name")
         now=datetime.now()
         print("current date and time",now)
         write_file(f_name="log.txt",txt=f"At {now} got name from adam")

         return self._name
    
    @name.setter
    def name(self,new_name):
         if not isinstance(new_name,str):
            print("Invalid name type")
            return
         now=datetime.now()
         print(f"Name set at {now} to {new_name} from {self._name}")
         write_file(f_name="log.txt",txt=f"At {now} got name from adam")
    
   
       

    

    def another_one(self,gender,name):
            print("This is another method")
            self._gender=gender
            self._name=name




adam=Human(name="Mathew",gender="male")
print("name",adam._name)
print("gender",adam._gender)
print("ribs",adam._ribs)

adam.another_one(name="Grace",gender="female")
print("name",adam._name)
print("gender",adam._gender)
print("ribs",adam._ribs)

print(adam.name)
