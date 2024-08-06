def binary_to_octal(element):
    while len(element) % 3 != 0:
        element = "0" + element
    octalVal = ""
    oct_bin_map = { '000': '0', '001': '1', '010': '2', '011': '3',
                    '100': '4', '101': '5', '110': '6', '111': '7'}
    while len(element) > 2:
        digit = element[(len(element)-3):len(element)]
        octalVal = oct_bin_map[digit] + octalVal
        element = element[:-3]
    return octalVal.lstrip("0")
element = input("enter binary value to convert into octal value:")
print(binary_to_octal(element))