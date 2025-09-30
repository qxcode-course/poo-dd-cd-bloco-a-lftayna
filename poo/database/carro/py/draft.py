class Carro:
    def __init__(self, pas: int, km: int, gas: int):
        self.passageiros: int = 0 
        self.km: int = 0
        self.gas: int = 0
        self.passMax: int = 2 
        self.gasMax: int = 100

    def enter(self) -> None:
        if self.passageiros < self.passMax:
            self.passageiros += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self) -> None:
        if self.passageiros > 0:
            self.passageiros -= 1
        else:
            print("fail: nao ha ninguem no carro")


    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"

def main():
    carro = Carro (" ", " ", " ")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(carro)
        if args[0] == "enter":
            carro.enter()
        if args[0] == "leave":
            carro.leave()

main()