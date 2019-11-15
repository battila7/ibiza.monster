def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


print(gcd(192, 72))

print(gcd_rec(192, 72))
