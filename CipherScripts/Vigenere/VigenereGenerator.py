#Vigenere main script
import Caesar

def cipherMatrixGenerator(baseAlpha):
    cipherMatrix = []
    for i in range(26):
        cipherMatrix.append(Caesar.shifter(i, baseAlpha))
    return cipherMatrix

def decodeCipher(cipherMatrix, decodeKey, cryptText, baseAlpha):
    j = -1
    decodedString = ""
    for i in range(len(cryptText)):
        decodeSet = ""
        if j >= len(decodeKey)-1:
            j = 0
        else:
            j+=1
        #print("j:", str(j))
        #print("len(decodeKey):", str(len(decodeKey)))
        for k in range(len(cipherMatrix)):
            temp = cipherMatrix[k]
            #print("temp[0]:", temp[0])
            if decodeKey[j] == temp[0]:
                #print("decodeKey[j]:", decodeKey[j])
                decodeSet = temp
                break
        #print("i:", str(i))
        #print("decodeSet.find(cryptText[i]):", str(decodeSet.find(cryptText[i])))
        #print("decodeSet:", decodeSet)
        #print("baseAlpha[decodeSet.find(cryptText[i]):", baseAlpha[decodeSet.find(cryptText[i])])
        decodedString += baseAlpha[decodeSet.find(cryptText[i])]

        #print("decodedString:", decodedString)
        #print()
    return decodedString


def main(baseAlpha, decodeKey, cryptText):
    cipherMatrix = cipherMatrixGenerator(baseAlpha)
    decodedText = decodeCipher(cipherMatrix, decodeKey, cryptText, baseAlpha)
    print(decodedText)
    return True

if __name__ == "__main__":
    baseAlpha = "abcdefghijklmnopqrstuvwxyz"
    main()
