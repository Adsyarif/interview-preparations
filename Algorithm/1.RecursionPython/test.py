def sumDigit(num):
    if num < 10:
        return num
    
    digit = num % 10 #5
    sisa = num // 10 #1234 
    return digit + sumDigit(sisa)

print(sumDigit(12345))