#Revmoe pass and complete the cat class
class Cat():
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def speak(self):
        return "Meow"
stella = Cat(name="Stella", age=7)
garfield = Cat(name="Garfield", age=50)
stella_speech = stella.speak()
garfield_speech = garfield.speak()
print(f"{stella.name} says: {stella_speech}")
print(f"{garfield.name} says: {garfield_speech}")
#mfkjedkfj

