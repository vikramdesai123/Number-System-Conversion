# Problem Statement –

# Joseph is learning digital logic subject which will be for his next semester. 
# He usually tries to solve unit assignment problems before the lecture. 
# Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. 
# Toggle all bits of it after the most significant bit including the most significant bit. 
# Print the positive integer value after toggling all bits”.

# Constrains-

# 1<=N<=100

# Example 1:

# Input :

# 10  -> Integer

# Output :

# 5    -> result- Integer

# Explanation:

# Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. 
# Hence output will print “5”.


def dec_to_binary(num:int) -> int:
    if num == 0:
        return 0
    else:
        # converted decimal to binary       
        numStr = ""
        while num >= 1:
            digit = num % 2
            numStr = str(digit) + numStr
            num = num // 2
        
        # replace 1 with 0 and 0 with 1        
        newNumStr = ""  
        for i in numStr:
            if i == "0":
                newNumStr=newNumStr+"1"
            else:
                newNumStr=newNumStr+"0"
        
        # converted binary to decimal        
        numInt = 0
        count = 0
        while len(newNumStr) > 0:
            char = newNumStr[(len(newNumStr)-1):len(newNumStr)]
            numInt = numInt + (int(char)*(2**count))
            count += 1 
            newNumStr = newNumStr[:len(newNumStr)-1]
        return numInt

num = int(input("Enter decimal value:"))
print(dec_to_binary(num))