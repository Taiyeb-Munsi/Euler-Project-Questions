# what is the largest prime factor of the number 600851475143

def f1(n):
    i = 2
    while i*i <= n:
        if n%i:
            i += 1
        else:
            n //= i

    return n

res = f1(600851475143)
print(res)
