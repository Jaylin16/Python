# python 추가 문법
# 1. tuple
# 2. 집합
# 3. f-string
# 4. 예외처리
# 5. 파일 불러오기
# 6. if문과 for문 한줄로 줄여쓰기 (feat. 삼항연산자와 향상된 for문 느낌)
# 7. map
# 8. lambda식
# 9. filter (결과값이 true인 값만 필터링)



# 1. tuple 튜플 (불변형 리스트)
# 리스트는 "[]"를 사용하지만 튜플은 "()"를 사용.

a = ('사과', '수박', '체리', '블루베리')
# 불변의 데이터이므로 아래와 같이 추가 또는 변경 등이 불가.
# a.append('과일')
# a [0] = '과일'



# 2. 집합 (중복을 제거)

a = ['사과', '수박', '체리', '블루베리', '블루베리', '블루베리']
a_set = set(a)

print(a_set)

## 1)교집합
a = ['사과', '수박', '체리', '블루베리', '블루베리', '블루베리']
b = ['수박', '체리']
a_set = set(a)
b_set = set(b)

print(a_set & b_set)

## 2)합집합
a = ['사과', '수박', '체리', '블루베리', '블루베리', '블루베리']
b = ['수박', '체리']
a_set = set(a)
b_set = set(b)

print(a_set | b_set)

## 3)차집합
a = ['사과', '수박', '체리', '블루베리', '블루베리', '블루베리']
b = ['수박', '체리']
a_set = set(a)
b_set = set(b)

print(a_set - b_set)



# 3. f-string (f'string 사이에 {변수}' 작성)
fruits = [
    {'name':'사과','price':1000},
    {'name':'수박','price':2000},
    {'name':'체리','price':3000},
    {'name':'블루베리','price':4000},
    {'name':'딸기','price':5000},
    {'name':'샤인머스캣','price':6000},
    {'name':'복숭아','price':7000}
]

for fruit in fruits:
    name = fruit['name']
    price = fruit['price']
    print(name + '의 가격은 ' + str(price) + '입니다.')
    print(f'{name}의 가격는 {price}입니다.')



# 4. 예외처리 (exception)
fruits = [
    {'name':'사과','price':1000},
    {'name':'수박','price':2000},
    {'name':'체리','price':3000},
    {'name':'블루베리'},
    {'name':'딸기','price':5000},
    {'name':'샤인머스캣','price':6000},
    {'name':'복숭아','price':7000}
]

for fruit in fruits:
    name = fruit['name']

    try:
        if fruit['price'] > 4000:
            print(f'{name}은/는 비싼 과일')
    except:
        print(f'{name}에서 error 발생')



# 5. 파일 불러오기
from function import *

choose_fruit()



# 6. if문과 for문 한줄로 줄여쓰기 (feat. 삼항연산자와 향상된 for문 느낌)

# if문 줄여쓰기
num = random_number()

result = ('짝수' if num % 2 == 0 else '홀수')
print(f'{num}은/는 {result}.')

# for문 줄여쓰기
a_list = [1,2,3,4,5]

result = [a+1 for a in a_list]
print(result)



# 7. map
fruits = [
    {'name': '사과', 'price': 1000},
    {'name': '수박', 'price': 2000},
    {'name': '체리', 'price': 3000},
    {'name': '블루베리', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '샤인머스캣', 'price': 6000},
    {'name': '복숭아', 'price': 7000}
]


def check_expensive(fruit):
    return '비싸!' if fruit['price'] > 4000 else '낫벳!'

result = map(check_expensive, fruits)
print(list(result))



# 8. lambda식
def check_expensive(fruit):
    return '비싸!' if fruit['price'] > 4000 else '낫벳!'

result = map(lambda x: '비싸!' if x['price'] > 4000 else '낫벳!', fruits)
print(list(result))



# 9. filter (결과값이 true인 값만 필터링)

expensive_fruit_list = filter(lambda fruit: fruit['price'] > 4000, fruits)

result = list(map(lambda x: x['name'], expensive_fruit_list))

print('비싼과일 리스트', result)