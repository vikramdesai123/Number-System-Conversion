def hexadecimal_to_decimal(element):
    if element == "0":
        return "0"

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
    return str(decimalVal)

element = input("Enter hexadecimal number to convert it into decimal:")
print(hexadecimal_to_decimal(element))
