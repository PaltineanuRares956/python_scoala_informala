def all_sum(n):
    if n == 0:
        return 0

    return n + all_sum(n - 1)

def even_sum(n):
    if n == 0:
        return 0

    if n % 2 == 1:
        return even_sum(n - 1)
    else:
        return n + even_sum(n - 1)

def odd_sum(n):
    if n == 0:
        return 0

    if n % 2 == 1:
        return n + odd_sum(n - 1)
    else:
        return odd_sum(n - 1)
