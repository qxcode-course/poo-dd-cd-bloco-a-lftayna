class Towel: 
    def __init__(self, color:str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None
        self.wetness += amount 
        self.wetness >= getMaxwetness():
        print("toalha emxarcada")
        self.wetness = getMaxwetness

    def getMaxwetness(self) -> int: 
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
            return 0

    def wringOut(self) -> None 
        self.wetness = 0

    def isDry(self) -> bool: 
            return self.wetness = 0
    
    def __str__(self) -> str: 
        return f"Cor: {self.color}, Tam: {self.size}, Umidade: {self.wetness}"

Minhatoalha: str = Towel (red, G)
print(Minhatoalha)