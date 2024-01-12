# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

class Member:
    __number = 0           # private : 자신의 클래스에서만 사용가능 / 없으면 public

    # 다른 언어에서는 메소드에 밖에 접근 못함, private와 static 메소드가 아니면 다른 언어에서 사용할 수 없음
    # 주로 자바에서 사용
    # 외부에서 접근하지 말자!
    # 외부에서 접근시 메소드로 접근하자!

    def __init__(self, id, pw, name):
        Member.__number += 1
        self.number = Member.__number
        self.id = id
        self.pw = pw
        self.name = name

    @staticmethod
    def get_number():
        return Member.__number

    @classmethod
    def admin(cls,**kwargs):
        kwargs['id'] = 'admin_' + kwargs['id']
        return cls(**kwargs)


member1 = Member.admin(id='heejookkk', pw='0122', name='diana')
print(member1.get_number())
member2 = Member.admin(id='heek',pw='0123', name='dian')
print(member2.get_number())

# class Member_Kwargs:
#     def __init__(self,**kwargs):
#         self.number = kwargs['number']
#         self.id = kwargs['id']
#         self.pw = kwargs['pw']
#         self.name = kwargs['name']
#         kwargs.get('number')
#
#     @classmethod
#     def admin(cls, id, pw, name, number=0):
#         number += 1
#         return cls('admin_'+id, pw, name, number)
#
# member1 = Member.admin(id = 'heejookkk',pw = '0122',name = 'diana')