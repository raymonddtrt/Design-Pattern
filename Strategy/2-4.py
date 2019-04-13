# 策略模式與簡單工廠結合
# 建立CashContext類別
class CashContext:
    def __init__(self,mode):
        self.mode = mode

    def choose(self):
        if self.mode == 1:
            return CashNormal()
        elif self.mode == 2:
            return CashRebate(0.8)
        elif self.mode == 3:
            return CashReturn(100,10)

    def getResult(self,money):
        return self.choose().acceptCash(money)

# 建立CashSuper類別
class CashSuper:
    def acceptCash(self,money):
        pass

# 建立CashNormal類別
class CashNormal(CashSuper):
    def acceptCash(self,money):
        return money

# 建立CashRebate類別
class CashRebate(CashSuper):
    def __init__(self,moneyRebate):
        self.moneyRebate = moneyRebate

    def acceptCash(self,money):
        return self.moneyRebate * money

# 建立CashReturn類別
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
    money = int(input("請輸入金額"))

    totalPrice = CashContext(mode).getResult(money)
    print(totalPrice)
# 程式入口
main()