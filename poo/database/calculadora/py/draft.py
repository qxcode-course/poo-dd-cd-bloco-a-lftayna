class Calculadora: 
    def __init__(self, battery: int, batteryMax: int, display: int):
        self.battery: int = 0
        self.batteryMax: int = 0
        display: int = 0.00
    
    def __str__(self) -> str:
        return f"pass: display = {display:.2f}, battery = {battery}"

    def calculator(self, batteryMax: int):
        print(batteryMax)
    
    def change(self, increment: int) -> None:

    def 
def main(): 
    calculadora = Calculadora
    while True:
        line: str = input()
        print('$' + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "init":
            print("init" + batteryMax)
        if args[0] == "show":
            calculadora.__str__()
        
        