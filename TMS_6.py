# def squere(x):
#     return x ** 2
#
#
# square_lambda = lambda x: x ** 2
#
# print(squere(4))
#
# print(square_lambda(4))
from itertools import product


# def add(a, b):
#     result = a + b
#     return result
#
#
# res = add(6, 6)
#
# print(res)

# def greet(name):
#     print(f"Hello {name}! Good morning!")
#
#
# greet("Maksim")

#
# def print_hello():
#     print("Hello")
#


# print_hello()

# def summa(a, b = 7):
#     result = a + b
#     return result
# print(summa(6))

#
# def say_hello(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#     for name in args:
#         print(f"Hello {name}!")
#     for beer, price in kwargs.items():
#         print(f"{beer}, {price}")
#
#
#
# say_hello("Maksim", "Polina", beer = 3, price=30)

#
# def new_order(**orders):
#     for customer, info in orders.items():
#         print(f"Поступил новый заказ от {customer}: {info['product']} кол-во  {info["quantity"]}")
#
# new_order(
#         Alex={"product": "Книга", "quantity": 2},
#         Maria={"product": "Книга", "quantity": 2}
#         )




#
# def my_shop(**kwargs):
#     for name, shop_item in kwargs.items():
#         print(f"Привет {name}! Ты оформил {shop_item['product']}, твой номер в очереди --- {shop_item['place']}")
#
#
#
# my_shop(
#     Max={"product": "Phone", "place": 2},
#     Maria={"product": "Ipad", "place": 5}
#
