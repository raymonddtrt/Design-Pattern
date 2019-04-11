#生成cashier類別
class Cashier:
    #建構式
    def __init__(self,price,amount):
        self.price = price
        self.amount = amount

    #用來顯示的方法
    def total(self):
        return Calculator(self.price,self.amount).calculate()

#簡麗calculate物件。用來計算，繼承Cashier
class Calculator(Cashier):
    #建構式，繼承Cashier才能把參數傳進來
    def __init__(self,price,amount):
        self.price = price
        self.amount = amount
    #計算
    def calculate(self):
        return self.price * self.amount

def main():
    price = input("請輸入單價:")
    amount = input("請輸入數量:")

    print(Cashier(int(price),int(amount)).total())

main()