def octal_to_Hexadecimal(element):
    newElement = int(element)
    
    if newElement == 0:
        return "0"
    
    # step-1 :octal to decimal
    
    decimalVal = 0
    count = 0
    while newElement > 0:
        digit = newElement % 10
        decimalVal = decimalVal + (digit*(8**count))
        newElement = newElement // 10
        count += 1 
    
    # step-2: decimal to hexadecimal 
    
    hexa = "0123456789ABCDEF"
    hexaVal = ""
    while decimalVal >= 1:
        digit = decimalVal % 16 
        hexaVal = hexa[digit] + hexaVal
        decimalVal = decimalVal // 16 
    return hexaVal
        
        
element = input("enter octal number to convert it into Hexadecimal number:")
print(octal_to_Hexadecimal(element))
