def octal_to_decimal(element):
    newElement = int(element)
    
    if newElement == 0:
        return "0"
    decimalVal = 0
    count = 0
    while newElement > 0:
        digit = newElement % 10
        decimalVal = decimalVal + (digit*(8**count))
        count += 1
        newElement = newElement // 10
    return (str(decimalVal))
        
element = input("enter octal number to convert it into decimal number:")
print(octal_to_decimal(element))