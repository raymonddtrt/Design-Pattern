# Person類別(ConcreteComponent)
class Person():
    def __init__(self,name = None):
        self.name = name

    def Show(self):
        print("裝扮的",self.name)

# 服飾類別(Decorator)
class Finery(Person):
    def Decorate(self,component):
        self.component = component
    def Show(self):
        if self.component != None:
            self.component.Show()

# 具體類別服飾(ConcreteDecorator)
class TShirts(Finery):
    def Show(self):
        print("大TShirt")
        super().Show()

class BigTrouser(Finery):
    def Show(self):
        print("垮褲")
        super().Show()

class Sneakers(Finery):
    def Show(self):
        print("破球鞋")
        super().Show()

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

    pqx = Sneakers()
    kk = BigTrouser()
    dtx = TShirts()

    pqx.Decorate(xc)
    kk.Decorate(pqx)
    dtx.Decorate(kk)
    dtx.Show()


if __name__ == '__main__':
    main()
