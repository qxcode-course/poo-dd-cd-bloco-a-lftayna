class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size 
        self.wetness: int = 0

    def dry(self,  amount: int) -> None:
        self.wetness += amount 
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness() #pq não tem : aqui? cadê o else?

    def getMaxWetness(self) -> int: 
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
        return f"Cor: {self.color}, Tam: {self.size}, Umidade: {self.wetness}"

    def main():
        toalha = Towel("", "") #obj manipulado
        while True: #looping infinito
            line:str = input() #entrada da linha
            args: list[str] = line.split("") #6 linha de palavras
            if args[0] == "end": #fim da execução
                break 
            elif args[0] == "new" #color size 
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
            elif args[0] == "show":
                print(toalha)
            elif args[0] == "dry": #amount 
                amount: int == int(args[1])
            toalha.dry(amount)
            else:
                print("fail")

Minhatoalha: str = Towel("rosa", "M")
print(Minhatoalha)
Minhatoalha.dry(3)
print(Minhatoalha)
Minhatoalha.dry(15)
Minhatoalha.dry(10)
print(Minhatoalha) 


