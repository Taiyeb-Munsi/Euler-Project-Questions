# Find the sum of all the primes under two million

def prime(num):
    if num <= 3:
        return num > 1

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

res = 0

for i in range(2, 2000000):
    if(prime(i)):
        res += i

print(res)
