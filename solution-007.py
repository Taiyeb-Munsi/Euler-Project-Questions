# What is the 10,001th prime number

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 6 
p = 13
result = 13

while count < 10001:
    p += 2
    if is_prime(p):
        count += 1
        result = p

print(result)
