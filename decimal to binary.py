def decimal_to_binary(element):
    if element == 0:
        return 0
    binaryNum = ""
    while element>=1:
        digit = element % 2
        binaryNum = str(digit) + binaryNum
        element = element // 2
    return binaryNum
element = int(input("Enter a decimal number to convert into binary:"))
print(decimal_to_binary(element))
