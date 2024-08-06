def octal_to_binary(element):
    intElement = int(element)
    if intElement == 0:
        return "0"
    
    octal_binary_map = {"0":"000","1":"001","2":"010","3":"011",
                         "4":"100","5":"101","6":"110","7":"111"}
    
    binaryVal = ""
    while intElement > 0:
        digit = intElement % 10
        binaryVal = octal_binary_map[str(digit)] + binaryVal
        intElement = intElement//10 
    return binaryVal.lstrip("0")


element = input("enter octal number to convert it into binary number:")
print(octal_to_binary(element))