class Program:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            print(self.num1+self.num2)
        elif self.operator == "-":
            print(self.num1-self.num2)
        elif self.operator == "*":
            print(self.num1*self.num2)
        elif self.operator == "/":
            print(self.num1/self.num2)


calculator = Program(3,5,"-")

print(calculator.calculate())