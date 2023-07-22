"""
The potency(k, n) function returns the value of k^n, where k and n are positive integers.

Function created based on the concept that k^n = k^(n-1) + k^(n-1).
"""
def potency(k, n):
    if n == 0:
        return 1
    elif n == 1:
        return k
    else:
        left = potency(k, n - 1)
        right = potency(k, n - 1)
        return left + right

# Example
print(potency(2, 0))
print(potency(2, 1))
print(potency(2, 2))
print(potency(2, 3))
print(potency(2, 4))
print(potency(2, 5))