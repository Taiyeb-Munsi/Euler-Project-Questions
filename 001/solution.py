def f(n, a1, an):
    return (n * (a1 + an)) // 2

res = f(333, 3, 999) + f(199, 5, 995) - f(66, 15, 990)

print(res)
