from math import sqrt as s
def is_prime(num):
    if num<= 1:
        return False
    for i in range(1,int(s(num))):
        if num % i ==0:
            return False
    
    
    return True

is_prime(2348923491)