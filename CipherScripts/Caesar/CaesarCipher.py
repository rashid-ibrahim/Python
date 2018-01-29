def shifter(shiftBy, baseAlpha):
    cryptAlpha = baseAlpha[shiftBy:] + baseAlpha[:shiftBy]
    return cryptAlpha

def main(baseAlpha):
    crypted = input("Enter text to be brute forced: ")
    decryptedArr = []

    cryptAlphaArr = []
    for i in range(len(baseAlpha)):
        cryptAlphaArr.append(shifter(i, baseAlpha))

    for i in range(len(cryptAlphaArr)):
        #cryptAlpha = shifter(i, baseAlpha)
        cryptAlpha = cryptAlphaArr[i]
        decryptedStr = ""
        for j in range(len(crypted)):
            for k in range(len(cryptAlpha)):
                if cryptAlpha[k] == crypted[j]:
                    decryptedStr += baseAlpha[k]
        decryptedArr.append(decryptedStr)
            
    for i in range(len(decryptedArr)):            
        print("decryptedArr["+str(i)+"]:", decryptedArr[i])
        print()
        
    return True

if __name__ == "__main__":
    print("Quick and dirty Caesar Cipher script so I don't have to do it by hand.")
    print()
    baseAlpha = "abcdefghijklmnopqrstuvwxyz"
    main()
