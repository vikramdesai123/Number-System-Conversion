def binary_to_decimal(n):
    if n == 0:
        return 0
    else:
        deci = 0
        count = 0
        while n>0:
            digit = n%2 
            deci = deci + (digit*(2**count))
            n = n //10
            count += 1
        return deci

n = int(input("enter binary number:"))
print(binary_to_decimal(n))