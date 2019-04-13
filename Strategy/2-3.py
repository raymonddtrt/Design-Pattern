# 使用策略模式
# CashContext類別
    # GetResult方法
class CashContext:
    def __init__(self,mode):
        self.mode = mode

    def getResult(self,money):
        return self.mode.acceptCash(money)

# CashSuper類別
    # acceptCash方法

class CashSuper():

    def acceptCash(self,money):
        pass

# CashNormal類別，繼承CashSuper
    # acceptCash方法
class CashNormal(CashSuper):

    def acceptCash(self,money):
        return money

# CashRebate類別，繼承CashSuper
    # acceptCash方法
class CashRebate(CashSuper):
    def __init__(self,moneyRebate):
        self.moneyRebate = moneyRebate

    def acceptCash(self,money):
        return self.moneyRebate * money

# CashReturn類別，繼承CashSuper
    # acceptCash方法
class CashReturn(CashSuper):
    def __init__(self,moneyCondition, moneyReturn):
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn

    def acceptCash(self,money):
        if money > self.moneyCondition:
            return money - (money/self.moneyCondition) * self.moneyReturn
        return money


# 用戶端程式碼
def main():
    mode = int(input("請輸入模式"))
    money = int(input("請輸入價格"))
    if mode == 1:
        cc = CashContext(CashNormal())
    elif mode == 2:
        cc = CashContext(CashRebate(0.8))
    elif mode == 3:
        cc = CashContext(CashReturn(100,10))
    print(cc.getResult(money))


# 程式入口
main()