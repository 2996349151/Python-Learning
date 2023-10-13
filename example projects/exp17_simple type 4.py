class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"I am {self.name}, and I am {self.age} now.")
        
class Mixin:
    def fly(self):
        print("I can fly.")
        
class pig(Mixin, Animal):
    def special(self):
        print("I am pig.")

p = pig("p",5)
p.say()
p.special()
p.fly()
