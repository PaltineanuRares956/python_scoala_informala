if __name__ == '__main__':

    my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

    print("The list sorted sorted ascending is {}".format(sorted(my_list)))
    print("The list sorted sorted descending is {}".format(sorted(my_list, key=None, reverse=True)))

    sorted_list = sorted(my_list)

    print(f"The even numbers are: {sorted_list[1::2]}")
    print(f"The odd numbers are: {sorted_list[::2]}")
    print(f"The numbers divisible by 3 are: {sorted_list[2::3]}")

