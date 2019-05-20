class Person:
    def __init__(self,name):
        self.name = name

    def WearTShirts(self):
        print("大TShirt ")

    def WearBigTrouser(self):
        print("垮褲 ")

    def WearSneakers(self):
        print("破球鞋 ")

    def WearSuit(self):
        print("西裝 ")

    def WearTie(self):
        print("領帶 ")

    def WearLeatherShoes(self):
        print("皮鞋 ")

    def Show(self):
        print("裝扮的",self.name)

#用戶端程式碼
def main():
    xc = Person("Orz")

    print("第一種裝扮")

    xc.WearTShirts()
    xc.WearBigTrouser()
    xc.WearSneakers()
    xc.Show()

    print("第二種裝扮")

    xc.WearSuit()
    xc.WearTie()
    xc.WearLeatherShoes()
    xc.Show()

main()

