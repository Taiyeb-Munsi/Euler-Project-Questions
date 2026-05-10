# Find the largest palindrome made from the product of two 3-digit numbers

def f2(n):
    if n%10 == 0:
        return 0
    
    temp = n
    sum = 0
    while n > 0:
        sum = (sum*10)+(n%10)
        n //= 10
    
    if temp == sum:
        return 1
    else:
        return 0

def f1():
    a = 0

    for i in range(101, 999):
        for j in range(i, 999):
            if f2(i*j):
                a = max(a, i*j)

    return a

res = f1()

print(res)
