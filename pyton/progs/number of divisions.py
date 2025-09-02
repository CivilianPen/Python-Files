def number_of_divisors(n):
    i = 1
    o = 0
    while i * i <= n:
        if n % i == 0 and i * i != n:
            o += 2
        elif n % i == 0 and i * i == n:
            o += 1
        i += 1
    return o

print(number_of_divisors(810810000))

