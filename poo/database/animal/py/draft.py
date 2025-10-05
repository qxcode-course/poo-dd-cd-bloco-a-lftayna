class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def makeSound(self):
        if self.age == 0:
            print('---')
        if self.age >= 4:
            print("RIP")
        if self.age > 0 and self.age < 4:
            print(self.sound)

    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4
           
    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal = Animal
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        if args[0] == "show":
            print(animal)
        if args[0] == "noise":
            animal.makeSound()
        if args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
main()


