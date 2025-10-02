class Carro:
    def __init__(self, passageiros: int, km: int, gas: int):
        self.passageiros: int = 0 
        self.km: int = 0
        self.gas: int = 0
        self.passMax = 2
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
        
    def fuel(self, increment: int):
        if self.gas < 100:
            self.gas += increment
            if self.gas > 100:
                self.gas = 100

    def drive(self, distance: int) -> None:
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if distance <= self.gas:
            self.km += distance
            self.gas -= distance
        else:
            kmpercorrido = self.gas
            self.km += kmpercorrido
            self.gas = 0
            print(f"fail: tanque vazio apos andar {kmpercorrido} km")
            
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
        if args[0] == "fuel":
            increment: int = int(args[1])
            carro.fuel(increment)
        if args[0] == "drive":
            distance: int = int(args[1])
            carro.drive(distance)

main()