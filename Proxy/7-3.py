# 代理介面
class IGiveGift:
    def GiveDolls(self):
        pass
    def GiveFlowers(self):
        pass
    def GiveChocolate(self):
        pass

# 追求者類別
class Pursuit(IGiveGift):
    def __init__(self,mm):
        self.mm = mm

    def GiveDolls(self):
        print(self.mm.name + " 送你洋娃娃")
    def GiveFlowers(self):
        print(self.mm.name + " 送你送你鮮花")
    def GiveChocolate(self):
        print(self.mm.name + " 送你巧克力")

# 代理類別
class Proxy(IGiveGift):

    def __init__(self,mm):
        self.gg = Pursuit(mm)

    def GiveDolls(self):
        self.gg.GiveDolls()

    def GiveFlowers(self):
        self.gg.GiveFlowers()

    def GiveChocolate(self):
        self.gg.GiveChocolate()

# 被追求者類別
class SchoolGirl:
    def __init__(self,name):
        self.name = name

# 用戶端程式碼
def main():
    jj = SchoolGirl("李嬌嬌")

    daili = Proxy(jj)

    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()

if __name__ == '__main__':
    main()