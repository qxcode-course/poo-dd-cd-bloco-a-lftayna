class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0 #isso não é um parametro, e sim uma variavel, o restante são parametros.

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness >= self.getMaxwetness():
            print("toalha encharcada")
            self.wetness = self.getMaxwetness()

    def wringOut(self) -> None:
        self.wetness = 0

    def getMaxwetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def isDry(self) -> bool:
        if self.wetness == 0:
            return True
        else: 
            return False

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
        toalha = Towel(" ", " ")
        while True:
            line: str = input()
            print("$" + line)
            args: list[str] = line.split(" ")
            if args[0] == "end":
                break
            if args[0] == "criar":
                color = args[1]
                size = args[2]
                toalha = Towel(color, size)
            if args[0] == "mostrar":
                print(toalha)
            if args[0] == "seca":
                print(f"sim" if toalha.isDry() else "nao")
            if args[0] == "enxugar":
                amount: int = int(args[1])
                toalha.dry(amount)
            if args[0] == "torcer":
                toalha.wringOut()
main()