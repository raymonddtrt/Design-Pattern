# coding=utf-8
# 簡單工廠模式的介紹及代碼實例
# 舉個加減乘除的例子
# 定義一個父類，預留接口
class Operation():
    def __init__(self, num1 = 0, num2 = 0):
        self.num1 = num1
        self.num2 = num2

class Add(Operation):
    def get_result(self):
        return self.num1 + self.num2

class Minus(Operation):
    def get_result(self):
        return self.num1 - self.num2

class Multi(Operation):
    def get_result(self):
        return self.num1 * self.num2


class Divide(Operation):
    def get_result(self):
        try:
           return self.num1/self.num2
        except:
           return '被除數不能為0，請重新輸入'

# 這個就是一個工廠，根據用戶的輸入選擇來調用相應的類去創建實例完成任務
class OptionFactory():
  def choose(self,op):
      
      if op == '+':
          return Add()
      if op == '-':
          return Minus()
      if op == '*':
          return Multi()
      if op == '/':
          return Divide()

# 根據用戶輸入來決定調用哪個類，這就是工廠類的作用
if __name__ == '__main__':
   ch = ''
   while not ch == 'q':
        num1 = int(input('Please input number1:  '))
        op = str(input('Please input the operation:  '))
        num2 = int(input('Please input number2:  '))
        OPFactory = OptionFactory()
        OPType = OPFactory.choose(op)
        OPType.num1 = num1
        OPType.num2 = num2
        print('The result is:', OPType.get_result())
        try:
            ch = str(input())
        except:
            ch = ''