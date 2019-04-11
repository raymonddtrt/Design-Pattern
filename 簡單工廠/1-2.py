class OperationFactory:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            return OperationAdd(self.num1,self.num2).add()
        elif self.operator == "-":
            return OperationSub(self.num1,self.num2).sub()
        elif self.operator == "*":
            return OperationMul(self.num1,self.num2).mul()
        elif self.operator == "/":
            return OperationDiv(self.num1,self.num2).div()

class OperationAdd(OperationFactory):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
        # return self.result

class OperationSub(OperationFactory):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sub(self):
        self.result = self.num1 - self.num2
        return self.result

class OperationMul(OperationFactory):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def mul(self):
        self.result = self.num1 * self.num2
        return self.result


class OperationDiv(OperationFactory):
    def __init__(self,num1,num2,):
        self.num1 = num1
        self.num2 = num2

    def div(self):
        if self.num2 == 0:
            return "不能除以0"
        else:
            self.result = self.num1 / self.num2
            return self.result


def Main():
    strNumberA = input("請輸入數字A:")
    strOperate = input("請輸入運算符號:")
    strNumberB = input("請輸入數字B:")
    try:
        strResult = OperationFactory(int(strNumberA),int(strNumberB),strOperate).calculate()
        print(strResult)
    except:
        print("輸入有誤")

Main()