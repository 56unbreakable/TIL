movies = ['Dark Knight', 'Harry Potter', 'Parasite','Matrix','La La Land']

# 영화 목록 출력
print("{0:=^30}".format("영화 목록"))
for i in movies:
    print(i)
print("{0:=^39}".format(""))

# 예매할 영화 선택
while True:
    choice = input('예매할 영화를 선택하세요 : ')
    if choice not in movies:
        print('=> 예매할 수 없는 영화입니다')
    else:
        print('=> {}를 선택하였습니다.'.format(choice))
        break

# 관람 인원 선택
while True:
    people = float(input('예매할 인원을 선택하세요 : '))
    if people <= 0:
        print('=> 잘못된 숫자입니다. 다시 입력해주세요')
    elif float.is_integer(people) != True:
        print('=> 관람인원수는 정수만 가능합니다')
    else:
        people = int(people)
        print('관람 인원수는 %d명입니다'%people)
        break
'''
try,execpt문을 활용
while True:
    try:
        people = int(input())
        if people <= 0:
            print('=> 잘못된 숫자입니다. 다시 입력해주세요')
        else:
            print('관람 인원수는 %d명입니다'%people)
            break
    except ValueError:
        print('=> 관람인원수는 정수만 가능합니다')
'''
# 할인권 사용
sale_dic = {'orange' : 2000, 'valentine' : 3000, 'christmas' : 4000, 'independence' : 5000}
wrong_code = False
sale_price = 0
while True:
    if wrong_code == True:
        sale = input('할인권을 다시 사용하시려면 y, 금액확인으로 가시려면 n을 눌러주세요 : ')
    else :
        sale = input('할인권을 사용하시려면 y, 금액확인으로 가시려면 n을 눌러주세요 : ')
    if sale == 'y':
        sale_code = input('할인권 코드를 입력해주세요 : ')
        if sale_code in sale_dic:
            wrong_code = False
            sale_price = sale_dic[sale_code]
            print('%d원 할인됩니다.'%sale_price)
            del sale_dic[sale_code]
            break
        else :
            print('존재하지 않는 할인권입니다')
            wrong_code = True
    elif sale == 'n':
        print('할인권을 사용하지 않았습니다')
        break
    else:
        print('잘못된 입력입니다')

# 결제내역 출력
original_price = 12000 * people
price_sum = original_price - sale_price
print('<예매 상세 내역>')
print("{0:=^39}".format(""))
print('영화 제목 : {}'.format(choice))
print('관람 인원 : {}명'.format(people))
print('합산 금액 : {}원'.format(original_price))
print('할인 금액 : {}원'.format(sale_price))
print("{0:-^39}".format(""))
print('실 결제액 : {}원'.format(price_sum))