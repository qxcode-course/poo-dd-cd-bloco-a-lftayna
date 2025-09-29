class Towel: 
    def __init__(self, color:str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount 
        if self.wetness >= self.getMaxwetness():
            print("toalha encharcada")
            self.wetness = self.getMaxwetness()
    

    def getMaxwetness(self) -> int: 
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def wringOut(self) -> None: 
        self.wetness = 0

    def isDry(self) -> bool: 
            return self.wetness == 0
    
    def __str__(self) -> str: 
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
    minhaToalha = Towel(" ", " ")
    while True: 
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            minhaToalha = Towel(color, size)
        elif args[0] == "mostrar":
            print(minhaToalha)
        elif args[0] == "torcer":
            minhaToalha.wringOut()
        elif args[0] == "seca":
            print("sim" if minhaToalha.isDry() else "nao")
        elif args[0] == "enxugar":
              amount: int = int(args[1])
              minhaToalha.dry(amount)
        else: 
            print("fail: codigo invalido")
main()