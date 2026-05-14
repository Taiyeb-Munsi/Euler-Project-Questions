# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import math

def prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False 

    return True

result = 1
power = 1

for i in range(2,20):
    if prime(i):
        for j in range(1,20):
            if i**j < 20:
                power = i**j

        result *= power

print(result)
