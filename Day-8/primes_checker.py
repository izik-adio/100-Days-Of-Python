from math import sqrt
# To check if a number is prime
def is_prime(num):
    if num <= 1:
        return "Not prime"
    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0:
            return "Not prime"
    return f"{num} is Prime".title()
print(is_prime(5))
