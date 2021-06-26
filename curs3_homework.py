def your_function(*args, **kwargs):
    ans = 0
    for arg in args:
        try:
            nr = float(arg)
        except ValueError:
            continue
        except TypeError:
            continue
        ans += nr
    return ans


print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))
print(your_function())
print(your_function(2, 4, "abc", param_1=2))


def read_inout():
    try:
        nr = int(input("Please provide an integer"))
    except ValueError:
        return 0
    except TypeError:
        return 0
    return nr


print(read_inout())

from curs3_homework_pkg import curs3_module

print(curs3_module.all_sum(3))
print(curs3_module.even_sum(10))
print(curs3_module.odd_sum(7))