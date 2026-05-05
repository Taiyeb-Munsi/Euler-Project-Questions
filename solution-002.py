# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def f(num):
    sum = 0
    t1, t2 = 1, 2
    i = 0
    while True:
        if t1 > num:
            break

        t1, t2 = t2, t1+t2 
        if i%3 == 0:
            sum += t1
        i += 1

    return sum 

n = 4000000
res = f(n)
print(res)
