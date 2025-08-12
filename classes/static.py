"""Module for Human class with getter and setter example."""

from datetime import datetime

def write_file(f_name, txt):
    """Append text to a file with utf-8 encoding."""
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")

class Human:
    """Represents a human with name, gender, ribs, and curse."""
    species = "H.sapiens"
    genus = "Homo"
    count = 0

    def __init__(self, gender, name):
        """Initialize a Human instance."""
        print("The initializer was called")
        self.gender = gender
        self._name = name
        if self.gender == "Male":
            self.ribs = 24
            self.curse = "Suffer"
        else:
            self.ribs = 23
            self.curse = "Pain"
        Human.count += 1

    @property
    def name(self):
        """Get the name of the human and log the access."""
        now = datetime.now()
        print("Current date and time", now)
        write_file(
            f_name="log.txt",
            txt=(
                f"At {now} got name from {self._name}"
            )
        )
        return self._name

    @name.setter
    def name(self, new_name):
        """Set the name of the human and log the change."""
        if not isinstance(new_name, str):
            print("Failed to update name")
            return
        now = datetime.now()
        print("Current date and time", now)
        write_file(
            f_name="log.txt",
            txt=(
                f"At {now} Name changed from "
                f"{self._name} to {new_name}"
            )
        )
        self._name = new_name

    def print_self(self):
        """Print details of the human."""
        print("----------------------")
        print("name", self.name)
        print("gender", self.gender)
        print("ribs", self.ribs)
        print("curse", self.curse)
        print("---------------------")

adam = Human(name="adam", gender="Male")
eve = Human(name="eve", gender="Female")

print("adam species", adam.species)
print("eve species", eve.species)
print("class property", Human.species)

print("Total humans", Human.count)