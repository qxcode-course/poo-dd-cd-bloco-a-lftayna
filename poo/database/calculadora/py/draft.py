class Calculadora:
    def __init__(self, batteryMax: int):
        self.display: float = 0
        self.batteryMax = batteryMax
        self.battery: int = 0

    def charge(self, value) -> None:
        if self.battery < self.batteryMax:
            self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def sum(self, a: int, b: int) -> None:
        if self.battery == 0:
            print(f"fail: bateria insuficiente")
            return
        else: 
            self.display = a + b
            self.battery -= 1

    def div(self, num: int, den: int):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        if den == 0:
            print("fail: divisao por zero")
            self.battery -= 1    
        else: 
            self.display = num / den
            self.battery -= 1

def main():
    calculdora = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            calculadora = Calculadora(int(args[1]))
        if args[0] == "show":
            print(calculadora)
        if args[0] == "charge":
            value: int = int(args[1])
            calculadora.charge(value)
        if args[0] == "sum":
            a: int = int(args[1])
            b: int = int(args[2])
            calculadora.sum(a, b)
        if args[0] == "div":
            num: int = int(args[1])
            den: int =int(args[2])
            calculadora.div(num, den)

main()
