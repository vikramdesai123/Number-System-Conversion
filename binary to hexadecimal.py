def binary_to_hexadecimal(element):
    if element == "0":
        return "0"
    while len(element) % 4 != 0:
        element = "0" + element
        
    binary_Hexa_map = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    HexadecimalVal = ""
    while len(element) > 3:
        digit = element[(len(element)-4):len(element)]
        HexadecimalVal = binary_Hexa_map[digit] + HexadecimalVal
        element = element[:-4]
    return HexadecimalVal.lstrip("0")

element = input("Enter value of binary number to convert into Hexadecimal value:")
print(binary_to_hexadecimal(element))