# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def f1(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def f2(n):
    return (n * (n + 1)) // 2

num = 100

res = f2(100)**2 - f1(100)

print(res)
