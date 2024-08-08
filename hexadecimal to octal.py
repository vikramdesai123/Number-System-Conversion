def hexadecimal_to_octal(element):
    if element == "0":
        return "0"
        
    # convert hexadecimal to decimal value

    hexa_map = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6",
                "7":"7","8":"8","9":"9","A":"10","B":"11","C":"12","D":"13",
                "E":"14","F":"15"}
    
    decimalVal = 0
    count = 0 
    
    while len(element) > 0:
        char = element[(len(element)-1) - len(element)]
        decimalVal = decimalVal + (int(hexa_map[char]) * (16 ** count))
        element = element[:len(element)-1]
        count += 1 
    
    # convert decimal to octal
    octalVal = ""
    
    while decimalVal >= 1:
        digit = decimalVal % 8 
        octalVal = str(digit) + octalVal
        decimalVal = decimalVal // 8 
    return octalVal

element = input("Enter hexadecimal number to convert it into octal value:")
print(hexadecimal_to_octal(element))
