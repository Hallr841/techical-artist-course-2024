total  = 1 
fib1 = 0
fib2 = 1

fibholder = fib1+ fib2q
while fibholder < 1000000:
    if fibholder % 2:
        total += fibholder
    fib1 = fib2
    fib2 = fibholder
    fibholder = fib1 + fib2

print(total)