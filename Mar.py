def caesarCipher():
    

    myString = input("what string whould you like me to incript?")
    shiftAmount =  int(input("Give me a shift amount"))
    cipherString = " "

    for c in myString:
        if c.isalpha():
            asciiValue = ord(c)
            asciiValue += shiftAmount

            if asciiValue < ord("a"):
                asciiValue -= 26

            if asciiValue > ord ("z"):
                asciiValue += 26
            
            x = chr(asciiValue)
            cipherString += x
    
    print(cipherString)

if __name__== "__main__":
    caesarCipher()        
