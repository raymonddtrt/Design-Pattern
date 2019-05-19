# 建立簡單工場類別
    # 方法 createOperate()
class OperationFactory:
    def createOperate(self,operate):
        if operate == "+":
            oper = OperationAdd()
        elif operate == "-":
            oper = OperationSub()
        elif operate == "*":
            oper = OperationMul()
        elif operate == "/":
            oper = OperationDiv()
        return oper


# 建立運算類別
    # 方法 GetResult()，屬性NumberA，NumberB
class Operation:
    def __init__(self,numberA = 0, numberB = 0):
        self.numberA = numberA
        self.numberB = numberB
    def GetResult(self):
        pass

# 建立加法類別
    # 方法 GetResult()
class OperationAdd(Operation):
    def GetResult(self):
        result = self.numberA + self.numberB
        return result

# 建立減法類別
    # 方法 GetResult()
class OperationSub(Operation):
    def GetResult(self):
        result = self.numberA - self.numberB
        return result

# 建立乘法類別
    # 方法 GetResult()
class OperationMul(Operation):
    def GetResult(self):
        result = self.numberA * self.numberB
        return result

# 建立除法類別
    # 方法 GetResult()
class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.numberA / self.numberB
        except:
            print("輸入有誤")
        return result

def main():
    operate = input("請輸入運算符號")
    oper = OperationFactory().createOperate(operate)
    oper.numberA = int(input("請輸入數字1: "))
    oper.numberB = int(input("請輸入數字2: "))
    result = oper.GetResult()
    print(result)

if __name__ == '__main__':
    main()
