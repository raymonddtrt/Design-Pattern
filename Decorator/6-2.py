# Person類別
class Person:
    def __init__(self,name):
        self.name = name

    def Show(self):
        print("裝扮的",self.name)

# 服飾抽象類別
class Finery:
    def Show(self):
        pass

# 各種服飾子類別
class TShirts(Finery):
    def Show(self):
        print("大TShirt")

class BigTrouser(Finery):
    def Show(self):
        print("垮褲")

class Sneakers(Finery):
    def Show(self):
        print("破球鞋")

class Suit(Finery):
    def Show(self):
        print("西裝")

class Tie(Finery):
    def Show(self):
        print("領帶")

class LeatherShoes(Finery):
    def Show(self):
        print("皮鞋")

# 用戶端程式碼
def main():
    xc = Person("Orz")
    print("第一種裝扮")
    dtx = TShirts()
    kk = BigTrouser()
    pqx = Sneakers()

    dtx.Show()
    kk.Show()
    pqx.Show()
    xc.Show()

if __name__ == '__main__':
    main()