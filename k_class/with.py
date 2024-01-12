class NameCard:

    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self     #필수
        # 객체 전에 할게 있으면 여기에 작성


    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit')
        # exception 이 여기에 담김


    def __del__(self):
        print('del')
        # 객체가 메모리에서 해제될때 del이 되고 해제됨


with NameCard() as name_card:
    name_card.print_info('강희주')