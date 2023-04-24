print('python 기본')

# '변수'는 어떠한 값의 메모리상 위치를 가리키는 것.
# '자료형' 종류 1. 숫자형, 2. 문자형, 3. 리스트형, 4. 딕셔너리형
# '기본 문법' 종류 5. 조건문, 6. 반복문, 7. 함수


# 1. 숫자형
# 변수 선언(숫자형)
a = 3
b = 2

# 기본 연산
print('덧셈:', a + b)
print('뺄셈:', a - b)
print('곱셈:', a * b)
print('나누기:', a / b)
print('제곱:', a ** b)
print('나눈 나머지:', a % b)



# 2. 문자형
# 변수 선언(문자형)
first = '첫번째'
second = str(2)
text = '123456'
email = 'example@email.com'

# 문자형 다루기
print('문자열 붙이기:', first + second)
print('문자열 길이:', len(text))
print('문자열 자르기(앞에서):', text[:3])
print('문자열 자르기(뒤에서):', text[3:])
print('문자열 자르기(구간):', text[3:5])
print('특정 문자 기준 자르기:', email.split('@')[1].split('.')[0])



# 3. 리스트형 (순서가 있는 자료형)
# 변수 선언(리스트형)
num_list = [1, 2, 3, 4, 5]
text_list = ['사과', '수박', '체리']
mix_list = [2, '사과', False, ['수박', '체리']]

# 리스트형 다루기
print('리스트에서 특정 인자 가져오기:', mix_list[3][0])
print('리스트 길이:', len(text_list))
print('리스트 자르기(앞에서):', num_list[:3])
print('리스트 마지막 인자 가져오기:', mix_list[-1])

# 리스트 추가, 정렬, 삭제
num_list.append(1)
num_list.sort()
num_list.sort(reverse=True)
num_list.remove(1)

# 리스트 내 특정 데이터 유무 확인
print('체리' in mix_list[3])
print('체리' in mix_list)



# 4. 딕셔너리형 (key-value 형태의 자료형)
# 변수 선언(딕셔너리형)
people_dict = {'name':'kitty', 'age':22}
mix_dict = {'name':'kitty', 'age':22, 'favorite':['체리','수박']}

# 딕셔너리형 다루기
print(people_dict['name'])
print(mix_dict['favorite'])

# 딕셔너리 추가, 정렬, 삭제
people_dict['new'] = 'newthing'
mix_dict['favorite'].append('블루베리')

# 딕셔너리 내 특정 데이터 유무 확인
print('수박' in mix_dict['favorite'])
print('수박' in mix_dict)



# 5. 조건문
# 작성시 유의할 점
# ':' 이후 들여쓰기가 있어야만 해당구간의 구문이 된다.
money = 3000

if money > 2500:
    print('초코우유!')
elif money > 1800:
    print('딸기우유!')
else:
    print('바나나우유!')



# 6. 반복문
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    name = person['name']
    age = person['age']
    if age > 20:
        print(name, age)

for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)
    if i > 3:
        break

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
max = 0

for num in num_list:
    if num > max:
        max = num

print(max)



# 7. 함수
def sum(a,b):
    print('더하기 실행')
    return a + b

result = sum(1,2)
print(result)

# 형변환
def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여자입니다.')
    else:
        print('남자입니다.')

check_gender('120101-10101010')
check_gender('120101-20101010')
check_gender('120101-30101010')
check_gender('120101-40101010')