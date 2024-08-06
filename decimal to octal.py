def decimal_to_octal(element):
    if element == 0:
        return 0
    else:
        octalNum = ""
        while element>= 1 :
            digit = element % 8 
            octalNum = str(digit) + octalNum
            element = element // 8 
        return octalNum
        
element = int(input("ENter a decimal number to convert into octal number:"))
print(decimal_to_octal(element))