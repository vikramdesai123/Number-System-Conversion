def decimal_to_hexadecimal(element):
    if element == 0:
        return 0
    # hexas = "0123456789ABCDEF"
    hexas = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hexadecimalNum = ""
    while element >= 1:
        digit = element % 16
        hexadecimalNum = hexas[digit] + hexadecimalNum
        element = element // 16 
    return hexadecimalNum
    
element = int(input("Enter decimal number to convert into hexadecimal:"))
print(decimal_to_hexadecimal(element))