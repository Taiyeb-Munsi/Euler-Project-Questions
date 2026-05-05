# Question :
Find the sum of all the multiples of 3 or 5 below 1000.

# Solution :
Total numbers divided by 3 under 1000 = 999/3    = 333
Total numbers divided by 5 under 1000 = 999/5   ~= 199
Total numbers divided by 15 under 1000 = 999/15 ~= 66

Result = (sum(3n) upto 333) + (sum(5n) upto 199) - (sum(15n) upto 66)
       = (3+6+..+999) + (5+10+..+995) - (15+30+..+990)
       = 333*(3+999)/2 + 199*(5+995)/2 - 66*(15+990)/2 
       = 233168
