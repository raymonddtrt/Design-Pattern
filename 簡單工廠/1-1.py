class Operation:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            return self.num1+self.num2
        elif self.operator == "-":
            return self.num1 - self.num2
        elif self.operator == "*":
            return self.num1 * self.num2
        elif self.operator == "/":
            return self.num1 / self.num2

def Main():
    strNumberA = input("請輸入數字A:")
    strOperate = input("請輸入運算符號:")
    strNumberB = input("請輸入數字B:")
    try:
        strResult = Operation(int(strNumberA),int(strNumberB),strOperate).calculate()
        print(strResult)
    except:
        print("輸入有誤")

Main()