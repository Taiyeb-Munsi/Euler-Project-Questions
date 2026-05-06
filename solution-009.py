# There exists exactly one Pythagorean triplet for which a+b+c = 1000. Find the product abc.

def f(n):
    for a in range(1, n):
        for b in range(a + 1, n // 2):
            c = n - a - b
            
            if a**2 + b**2 == c**2:
                print(f"Found: a={a}, b={b}, c={c}")
                return a * b * c

print(f(1000))
