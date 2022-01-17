class CAccount:
    menu_on = False    # 비밀번호를 틀렸을 때 다시 메뉴를 물어보지 않기 위해 사용하는 변수. 메뉴를 선택했을 경우 True
    trade_fail = False # 잔액 부족일 시 바로 프로그램을 종료하기 위한 변수

    def __init__(self, owner,password): # 클래스의 인자를 받아옴
        self.owner = owner
        self.amount = 0
        self.password = password
    
    def deposit(self): # 입금함수
        while True: 
            try : 
                money = int(input('입금할 금액을 알려주세요 : ')) # 입금할 금액을 받음
                if money > 0: # 금액이 양수일 경우
                    self.amount += money # 잔고에 더함
                    print('{}원이 입금되었습니다. 잔액은 {}원 입니다.'.format(money,user_account.amount))
                    self.menu_on = False # 메뉴로 다시 돌아가기 위해 False로설정
                    break # 잔고에 더했으니 루프 탈출
                else : # 잘못된 값일 경우
                    print('정확한 금액을 입력하세요') # 메세지 출력 후 다시 입력
            except : # 잘못된 값을 입력했을 경우 다시 입력하기위함 모든 에러에 대해 예외처리
                print('정확한 금액을 입력하세요') # 메세지 출력 후 다시 입력
    
    def withdraw(self): # 출금함수
        while True:
            try :
                money = int(input('출금할 금액을 알려주세요 : ')) # 출금할 금액을 받음
                if money >0 and self.amount >= money: # 출금액이 양수고 잔고보다 많을 경우
                    self.amount -= money # 잔고에서 뺌
                    print('{}원이 출금되었습니다. 잔액은 {}원 입니다.'.format(money,user_account.amount))
                    self.menu_on = False # 메뉴로 다시 돌아가기 위해서 False로 설정
                    break # 잔고에서 뺐으니 루프 탈출
                elif money >0 and self.amount < money: # 만약 잔액이 부족할 경우
                    print('잔액부족, 거래가 거절되었습니다.') # 메세지 출력 후 프로그램을 종료해야함
                    self.trade_fail = True # 프로그램을 끝내기 위해서 True로 설정
                    break # 루프 탈출
                else :
                    print('정확한 금액을 입력하세요.')  # 그 외 잘못된 값 입력시
            except :
                print('정확한 금액을 입력하세요.')  # 출금액을 다시 입력하게만듦

user_account = CAccount('hill',1234)  # 유저 정보 설정

print('{} 통장'.format(user_account.owner)) 
print('---------------------------------------')
print('''1. 잔액 확인
2. 입금
3. 출금
4. 종료
''')
print('----------------------------------------')
password = 0 # 패스워드의 초기화
password_on = False # 패스워드가 일치할 경우 다시 입력하지 않게 하기 위한 변수. 초기값을 False로 설정
menu_list = [1,2,3,4] # 잘못된 메뉴를 눌렀을 경우 다시 누르기 위한 메뉴 리스트
menu_wrong = False # 잘못된 메뉴를 눌렀으면 T, 아닐경우 F
while user_account.trade_fail == False: # 만약 잔액이 부족해서 거래가 거절되지(거절됐으면 True) 않았으면 실행
    if user_account.menu_on == False: # 만약 메뉴를 선택하지 않았다면 실행
        try :
            menu = int(input('메뉴를 선택해주세요 : ')) # 메뉴 선택
            if menu not in menu_list: # 만약 메뉴가 잘못된 숫자로 입력되면
                print('잘못된 입력입니다. 다시 입력하세요.') # 메세지 출력
                password_on = True # 비밀번호 입력을 생략하고 다시 메뉴 입력으로 돌아옴
                menu_wrong = True
            elif menu in menu_list and menu_wrong == True : # 제대로 메뉴를 입력했지만 이전에 틀린적이 있을 경우
                password_on = False # 비밀번호를 입력하지 않은 것으로 설정하고(이전에 틀렸을때 비밀번호를 입력한것으로 설정했기 때문)
                user_account.menu_on = True # 메뉴를 입력한것으로 판단하고 다음 스텝 실행
                menu_wrong = False # 메뉴를 틀린적 없음으로 변경.
            else : # 만약 처음부터 제대로 입력했을 경우
                user_account.menu_on = True # 메뉴를 입력한것으로 판단하고 다음 스텝 실행
        except : # 만약 에러가 날시
            print('잘못된 입력입니다. 다시 입력하세요.') # 메세지 출력
            password_on = True # 비밀번호 입력을 생략하고 다시 메뉴 입력
            menu_wrong = True # 비밀번호 입력을 생략하고 다시 메뉴 입력으로 돌아옴
    if password_on == False: # 비밀번호 입력이 되어있지 않은 상태이면
        password = int(input('비밀번호를 입력해주세요 : ')) # 비밀번호 입력
    if password == user_account.password: # 비밀번호가 일치하면
        password_on = True # 비밀번호를 입력한 상태로 만들고
        if menu == 1: # 1번메뉴를 고를시
            print('잔액은 {}원 입니다'.format(user_account.amount)) # 메세지 출력
            user_account.menu_on = False # 메뉴선택을 초기화해서 다시 메뉴 선택하게 만듦
        elif menu == 2: # 2번메뉴 고를시
            user_account.deposit() # 함수실행
        elif menu == 3: # 3번메뉴 고를 시
            user_account.withdraw() # 함수 실행
        elif menu == 4: # 4번메뉴 고를 시
            print('계좌거래가 종료되었습니다. ') # 메세지 출력
            break # 루프 탈출, 프로그램 종료
    elif password == 0: # 비밀번호가 초기값이라는 것은 아직 입력을 하지 않은 상태이므로 
        pass # 아무것도 실행하지않고 넘어감.
    else : # 만약 비밀번호가 잘못될 경우 다시 비밀번호 입력
        print('잘못된 비밀번호입니다. 다시 입력하세요.')
