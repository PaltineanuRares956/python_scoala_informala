print("Cursul 2")

name = "un nume"

if name:
    print(name)
else:
    print("Nu avem definit niciun nume")

first_person = {"Name" : "John"}
second_person = {"Name" : "John"}

if first_person is second_person:
    print("They are the same")
else:
    print("They are not the same")

if first_person == second_person:
    print("They are the same")
else:
    print("They are not the same")

# invalid
# name[2] = 'c'

print(ord('a'))

my_str = 'Owner\'s manual'
print(my_str)

print(r'Owner\'s manual')
nume = "Victor"
age=12
msg = "{0} has {1} years".format(nume, age)
print(msg)

msg_2 = f"{nume} has {age+7} years"
print(msg_2)



my_list = [1,2,3,"Ana are mere", True, False, None, {'a':1,'b':2}]
print(my_list[7]['a'])

my_list[3] = "New value"

inventar = ["faina", "drojdie", "apa", "sare"]

for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f"{value} : {index}")

print(inventar[-1])
print(f"The length of inventar is {len(inventar)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::-1])

l1 = [2, 3, 0, -6, -3]
# l.sort()
print(l1)
print(sorted(l1))

l2 = [3, [9, 10, 4]]
l1 = l1 + l2
print(l1)

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}

for key, val in my_dict.items():
    print(f"{key}->{val}")

print(my_dict.get(5, "Empty"))


my_set = {"First", "Second", None, True, 7, True, -1, 7}
print(my_set)

listtt = [1, 8, 5, 4, -1, 1]
print(set(listtt))

l1 = [1,2,34]
l2 = [2,3,5]

s1 = set(l1)
s2 = set(l2)

print(s1 - s2)
print(f"Union {s1 | s2}")
print(f"Intersection {s1 & s2}")

