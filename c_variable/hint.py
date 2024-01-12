from typing import List, Dict, Set, Tuple, Union, Final

data: Final[int] = 10 # final = 변경하지 마시오
print(data)


class A:
    pass

class B:
    def test(data: Union[int, str], number:int|float, data1:A,datas : List[int],data_dict:Dict[str:int])-> int:
    #union 여러개가 가능할 때, | 는 3.10버전부터사용가능
    # return type = -> 다음에 적음
        return 10