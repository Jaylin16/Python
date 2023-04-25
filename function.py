import random

fruits = [
    {'name': '사과', 'price': 1000},
    {'name': '수박', 'price': 2000},
    {'name': '체리', 'price': 3000},
    {'name': '블루베리', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '샤인머스캣', 'price': 6000},
    {'name': '복숭아', 'price': 7000}
]


def choose_fruit():
    fruit = random.choice(fruits)
    name = fruit['name']
    price = fruit['price']

    print(f'{name}이/가 먹고 싶다면 {price}원을 내!')


def random_number():
    num = random.randint(1, 10)

    return num
