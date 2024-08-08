def hexadecimal_to_binary(element):
    if element == "0":
        return "0"
    
    hexa_map = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110",
                "7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101",
                "E":"1110","F":"1111"}
    binaryVal = ""
    while len(element) > 0:
        char = element[(len(element)-1): len(element)]
        binaryVal = hexa_map[char] + binaryVal
        element = element[:len(element)-1]
    return binaryVal
    
element = input("Enter hexadecimal number to convert it into binary value:")
print(hexadecimal_to_binary(element))
