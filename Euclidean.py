'''
    Get greatest common divisor of two nonnegative integers
'''
def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)

result1 = gcd(24, 30)
result2 = gcd(12, 6)
print(result1, result2)