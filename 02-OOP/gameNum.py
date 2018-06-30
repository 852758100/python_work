import random
import math


class GameNum():

    def randomLine(self):

        s = ""
        for j in range(4):
            s = s + chr(random.randrange(65,91))

        for i in  range(8):
            s = s + str(random.randrange(10))

        return s
    print('game starting!')

    def enterIt(self,score):
        while   1:
            yNum = input("请输入三位数字参与游戏,输入-1结束游戏:")
            if yNum == str(-1):
                break

            if yNum.isdigit() and 100<=int(yNum)<=999:
                yNum = int(yNum)
                if yNum > random.randrange(100,1000):

                    print('你出入的数字百位,十位,个位依次为:', yNum//100, yNum%100//10, yNum%100%10)

                elif yNum == random.randrange(100,1000):
                    score += 100
                    print("您的得分为%d"%score)
                else:
                    for i in range(10):
                        s = self.randomLine() #当类调用时需要写上self 不然会报错,实例化调用时,则不需要写上self,写上会报错.

                        with open('str_num.txt', 'a') as f:
                            f.writelines(s + '\n')
                    print('写入10个12位字符串')
            else:
                print("您输入的不符合规则,烦请烦请重新输入")


if __name__ == '__main__':
    score = 0
    # GameNum.enterIt(GameNum,score)

    gam = GameNum()
    gam.enterIt(score)