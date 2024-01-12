# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
# # 회원 번호는 자동 증가한다.
# number = len(user_info)
# def set_user():
#
#     def insert(name):
#         global number
#         number += 1
#         user_info.append({'number': number, 'name': name})
#
#
#     # 목록
#     def select_all():
#         return user_info
#
#
#     # 조회(번호로 조회)
#     def select(number):
#         for user in user_info:
#             if user['number'] == number:
#                 return user
#         return {}
#
#
#     # 수정(번호로 이름 수정)
#     def update(**kwargs):
#         '''
#
#         :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#         '''
#         select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
#     # 삭제(번호로 삭제)
#     def delete(number):
#         del user_info[user_info.index(select(number))]
#
#     return {'insert':insert,'select': select, 'update':update,'delete': delete }
#
#
# user_service = set_user()
# user_service.get('insert')('han')
# print(user_service.get('select')(6))
# ----------------------------------------------------------------

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
number = len(post_info)                             # given value =length of the value, non-given = 0
                                                    # if number locate in fuction, whenever function runs, number is initialized
def set_post():                                     # closure () - value=post_info (already given)

    def insert(**kwargs):                           # function name : insert (input : type dict)
        global number                               # number in global area ? - prevent initialize
        number += 1                                 # accumulate number (1)
        post_info.append({
            "number": number,
            "title,":kwargs.get("title"),
            "content":kwargs.get("content"),
            "file":kwargs.get('file'),
            "read_count":0
        })                                          # organized by line, insert information / 'read_count' must be 0


    # 목록(최신순으로 조회) (역순으로 slicing)
    def select_all():                               # function name select_all
        print(post_info[::-1])                      # show the list of values from end(end =  newest)

    # 조회(번호로 조회, 조회수 1 증가)                   # To understand this, read  select funtion first
    def read(number):                               # function name read, selected by number named number
        post = select(number)                       # post(name) = using return value of function select = dict post
        post['read_count'] += 1                     # read dict post and find key 'read_count' and accumulate 1
        return post                                 # return dict post(name)

    def select(number):                             # funtion name select, select value by number named number
        for post in post_info:                      # reputation fine dict(value) post in post_info(list)
            if post["number"] == number:            # if the Key number == number that I put
                return post                         # return dict(value) post(name)

    # 수정(번호로 정보 수정) title,content,file 수정 가능
    def update(**kwargs):                           # function name update(need value as dict type)
        '''                                         
        :param kwargs:
        {
            'number': '수정할 번호',
            title': '수정할제목',
            'content': '수정할내용',
            'file':'수정할 첨부파일 주소'
        }
        '''                                         # function information
        post = select(kwargs.get('number'))         # post(decla) use select function, get dict value in input by key 'number'
        post['title'] = kwargs.get('title')         # dict value = value in post_inf, modify value of title to title(input)
        post['content'] = kwargs.get('content')     # modify value of content to content(input)
        post['file'] = kwargs.get('file')           # modify value of file to file(input)


    # 삭제(번호로 삭제)
    def delete(number):                            # function name : delet e
        del post_info[post_info.index(select(number))]  # select(number) = dict value post(have input number)
                                                        # post_info.index(value) - value = dict post(have input #)
                                                        # post_info[index number] of dict post
                                                        # delete that value

    return {'insert':insert,'read':read,'select_all': select_all, 'update':update,'delete':delete}
    # set return as a dict b/c
        # return is for closure, return must have all kinds of returns for each function
        # for the usage, type dict is more comfortable?


# usage
post_service = set_post()                           # for the usage of dict return, declaration post_service
                                                    # post_service = type dict
                                                    # get(key) of function, input value for key function
print(post_service.get('read')(4))
post_service.get('insert')(title='제목입니당',content='내용입니당',file='찾아보세여')
post_service.get('select_all')()