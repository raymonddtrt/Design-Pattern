# 簡單工廠模式
# 建立一個CashFactory類別

class CashFactory:
    def __init__(self, mode):
        self.mode = mode

    def createCashAccept(self):
        if self.mode == 1:
            return CashNormal()
        elif self.mode == 2:
            return CashRebate(0.8)
        elif self.mode == 3:
            return CashReturn(100,10)
# 建立一個CashSuper運算部門

class CashSuper:

    def acceptCash(self,money):
        pass

# 正常收費子類別，繼承於CashSuper
class CashNormal(CashSuper):

    def acceptCash(self,money):
        return money

# 打折收費子類別，繼承於CashSuper
class CashRebate(CashSuper):
    def __init__(self,moneyRebate):
        self.moneyRebate = moneyRebate

    def acceptCash(self,money):
        return self.moneyRebate * money

# 紅利收費子類別，繼承於CashSuper
class CashReturn(CashSuper):
    def __init__(self,moneyCondition, moneyReturn):
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn

    def acceptCash(self,money):
        if money > self.moneyCondition:
            return money - (money/self.moneyCondition) * self.moneyReturn
        return money
# 用戶端程式
def main():
    mode = input("請輸入模式")
    money = input("請輸入金額")

    csuper = CashFactory(int(mode)).createCashAccept()
    totalPrices = csuper.acceptCash(int(money))
    print(totalPrices)
# 程式入口
main()