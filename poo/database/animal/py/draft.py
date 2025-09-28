class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def makeSound(self): 
        if self.age == 0:
            print("---") 
        if self.age >= 4:
            print("RIP")
        if self.age > 0 and self.age < 4:
            print(self.sound)
    
    def ageBy(self, increment: int) -> int:
        self.age += increment
        self.age >= MaxAge()
        print("warning {species} morreu")
        self.age = MaxAge()

    def __str__(self) -> str:
        return f("")


meuAnimal = Animal("cachorro", "auau") 
print(meuAnimal)

