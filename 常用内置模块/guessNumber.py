import random
import math

guessBig = random.randint(0,1)


num = input('请输入一个三位数与电脑出的三位数随机比大或比小:')

if num.isdigit() and 100<=int(num)<=999:
    pkNum = random.randrange(100,999)

    if int(num)==pkNum:
        print("电脑出的数是:", pkNum, '比你出的数%s一样大' % num, 'no winner!')
    if guessBig:
        if int(num)>pkNum:
            print('比大','电脑出的数是:',pkNum,'你出的数是:',num, 'you win!')
        else:
            print("比大,电脑出的数是:", pkNum, '比你出的数%s小' % num, 'you lose')

    else:
        if int(num)<pkNum:
            print('比小','电脑出的数是:',pkNum,'你出的数是:',num,'you win!')
        else:
            print("比大,电脑出的数是:", pkNum, '比你出的数%s小' % num, 'you lose')


else:
    print('请按规则输入数字')
