import calc_add
# import calc_sub 같은 경로가 아니기 때문에 찾을 수 없다.
 #같은 경로가 아닐경우 패키지 명.모듈명 으로 경로 순서에 맞게 불러온다.
# import calc.calc_sub
# import calc.calc_sub as sub
from calc.calc_sub import sub
from calc.calc import Calculator

import os
import sys


# 완전 외부에 있는 모듈은 패키지가 아닌 path에서 찾기 떄문에 사용 가능하지만 설치시 path를 설정해주어야한다
if __name__ == '__main__':
    print(calc_add.add(1,3))
    # print(calc.calc_sub.sub(10,5))
    # print(sub.sub(4.5))
    print(sub(1,2))
    print('='*10)
    c = Calculator(10,5)
    print(c.add())
    print(c.sub())


    print(sys.path)
    print(os.path.abspath(os.path.dirname(__file__)))
    # 현재경로의 절대경로를 찾음 문자열 값, 여기에 파일이름을 더해주면 해당 파일을 객체로 가져올 수 있다.
    # print(sys.path.append(os.path.abspath(os.path.dirname(__file__))))
