# import random
#
# elements = [x for x in range(11)]
# print(elements)
#
# while True:
#     random_choice = random.choice(elements)
#     if random_choice % 3 == 0:
#         break
#     print(f"Random choice is {random_choice}")
#
# print(f"Exit random choice is {random_choice}")

# for i in range(11):
#     if i % 2 != 0:
#         continue
#     print(f"Even number {i}")

# my_sum = 0
#
#
# def get_sum(a, b):
#     global my_sum
#     my_sum = a + b
#     print(my_sum)
#
#
# get_sum(4, 5)
# print(my_sum)

# l1 = [1, 2, 3]
# l2 = l1
# l2.append(4)
#
# print(l1)
# print(l2)

# def my_func(nume, prenume, *args, **kwargs):
#     tail = ' '.join(args)
#     print(f"{nume} {prenume} {tail}")
#
#     for key in kwargs.keys():
#         print(f" {key} : {kwargs[key]}")
#
#
# my_func("Popescu", "Ana", "are", "2", "mere", job="developer", age=22)

# while True:
#     my_var = input("Introduceti un numar: ")
#
#     try:
#         my_int = int(my_var)
#         print(my_int)
#         if my_int > 10:
#             break
#     except ValueError as e:
#         print("Please enter an integer")
#     except NameError:
#         print("Undefined var")
#     else:
#         print("No exception")
#     finally:
#         print("This will be printed wheter or not an excepion occured")

# NAMESPACE - LOCAL
# msg = "coco"
#
#
# def my_func():
#     global msg
#     msg = "Hello world"
#     print(msg)
#
#
# print(msg)
# my_func()


#NAMESPACE - ENCLOSING

# def my_func():
#     def my_second_func():
#         print(f"My second function {msg}")
#
#     msg = "Hello world"
#     my_second_func()
#
# my_func()