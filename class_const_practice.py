class Person:
    def __init__ (self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

james = Person("James")
james.talk()

bob = Person("Bob Smith")
bob.talk()