# 追求者類別
class Pursuit:
    def __init__(self,mm):
        self.mm = mm

    def GiveDolls(self):
        print(self.mm.name + " 送你洋娃娃")
    def GiveFlowers(self):
        print(self.mm.name + " 送你送你鮮花")
    def GiveChocolate(self):
        print(self.mm.name + " 送你巧克力")

# 被追求者類別
class SchoolGirl:
    def __init__(self,name):
        self.name = name

# 用戶端程式
def main():
    jj = SchoolGirl("李嬌嬌")

    zjy = Pursuit(jj)

    zjy.GiveDolls()
    zjy.GiveFlowers()
    zjy.GiveChocolate()

if __name__ == '__main__':
    main()