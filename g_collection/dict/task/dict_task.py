# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "카페 메뉴"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

# 제목 출력
print(title)
# 무제한 반복
while True:
    # 메뉴의 숫자를 입력하는 변수
    choice = int(input(menu))
    # 추가
    # 메뉴에 1을 입력하였을 때
    if choice == 1:
        # 사용자에게 상품 이름과 가격을 한번에 입력받은 후 이름과 가격으로 나누어 각각의 변수에 담기
        name, price = input(append_message+"\n").split()
        if name not in data_dict:
            data_dict[name] = int(price)
            continue
        else:
            # 입력받은 상품명이 중복이라면 에러 메세지 출력
            result_message = append_error_message
    # 수정
    # 메뉴에 2를 입력하였을 때
    elif choice == 2:
        # 수정할 상품명 검색
        modify = input(search_name_message_for_update+"\n")
        # 수정할 상품명이 딕셔너리에 있다면 아래 에러 메세지 출력
        if modify not in data_dict:
            result_message = update_error_message1
        else:
            new_name, new_price = input(update_message+'\n').split()
            # 새로운 이름이 이미 딕셔너리에 있으면
            if new_name in data_dict:
                # 이미 있는 상품명이라는 메세지 출력
                result_message = update_error_message2
            # 수정할 상품명이 이름이 딕셔너리에 없으면
            # 키와 값  추가
            else:
                del data_dict[modify]
                data_dict[new_name] = int(new_price)

    # 삭제
    # 3번을 눌러 삭제 메뉴
    elif choice == 3:
        # 삭제할 상품명을 입력받음
        delete = input(delete_message+"\n")
        # 삭제할 상품명이 이름 리스트에 있다면
        if delete in data_dict:
            # 해당 상품명과 값 삭제
            del data_dict[delete]
            # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
            continue
        # 삭제할 상품명이 이름 리스트에 없다면 오류메세지 출력
        else:
            result_message = delete_error_message
    # 검색
    # 4번을 눌러 검색 메뉴
    elif choice == 4:
        # 검색할 메뉴를 선택하기 위해 입력받은 문자열을 정수로 변환하여 선언
        search_choice = int(input(search_menu+"\n"))
        # 검색할 메뉴 선택
        if search_choice == 1:
            # 검색한 상품명을 변수에 담음
            name_for_search = input(search_name_message+'\n')
            # 만약 상품명이 이름 리스트에 있다면
            if name_for_search in data_dict:
                for name, price in data_dict.items():
                    if name == name_for_search:
                        print(f'{name},{price}')
                # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                continue
            # 상품명이 이름 리스트에 없다면 에러 메세지 출력
            else:
                result_message = search_name_error_message
        # 검색할 메뉴 선택 2
        elif search_choice == 2:
            check = False
            # 가격을 검색하는 경우에는 가격을 입력 받아 정수로 변환하여 변수로 선언
            price_for_search = int(input(search_price_message+"\n"))
            # 최소 값 선언 (-50%)
            min = price_for_search * 0.5
            # 최대 값 선언 (+50%)
            max = price_for_search * 1.5
            for name, price in data_dict.items():
                if min <= price <= max:
                    check = True
                    print(f'{name},{price}')
            if check:
                continue
            if not check:
                result_message = search_error_message
        # 검색 메뉴의 1,2를 입력하지 않은 경우 오류메세지 출력
        else:
            result_message = error_message

    # 목록
    # 5번을 입력하여 목록메뉴
    elif choice == 5:
        # 이름 리스트에 값이 없는 경우 (입력한 상품명이 없는경우)
        if len(data_dict) == 0:
            # 에러 메세지 출력
            result_message = no_item_message
        # 이름 리스트에 값이 있는 경우 (입력한 상품명이 있는 경우)
        else:
            # 입력한 상품명의 갯수만큼 목록 출력
            for name, price in data_dict:
                print(f'{name},{price}')
                # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                continue
    # 나가기
    # 6번을 눌러 나가기 메뉴
    elif choice == 6:
        # 전체 반복에서 나가기
        break
    # 그 외
    # 메뉴 선택시 1~6 이외의 값을 넣은 경우
    else:
        # 오류 메세지 출력
        result_message = error_message
    # 결과 값 출력
    print(result_message)

