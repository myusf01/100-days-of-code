# week 2 function exercice

def isIna(char, aStr):
    def chckChar(aStr):
        if len(aStr) == 0:
            zero = "Please add an string that is bigger than 1"
            return zero

        elif len(aStr) == 1:
            return aStr
        else:
            return aStr

    def chckStr(char, aStr):
        midChar = int(len(aStr) / 2)
        if len(aStr) >= 1:
            if len(aStr) == 1:
                return aStr
            else:
                if str(char) < str(aStr[midChar]):
                    chckStr(char,aStr[:midChar])
                    # print("1")
                    # print(char)
                    # print(aStr[midChar])
                elif str(char) > str(aStr[midChar]):
                    chckStr(char,aStr[midChar:])
                    # print("2")
                    # print(char)
                    # print(aStr[midChar])

                else:
                    return True

    return chckStr(char,chckChar(aStr))




def isIn(char, aStr):
    midChar = int(len(aStr) / 2)


    if len(aStr) == 0 or (len(aStr) == 1 and char != aStr):
        print("first if")
        return False
    elif str(char) == str(aStr[midChar]):
        print("2nd")
        print(aStr[midChar])
        return True
    else:
        print("else")
        if str(char) > str(aStr[midChar]):
            print("first is else")
            return isIn(char, aStr[midChar:])

        elif str(char) < str(aStr[midChar]):
            print("2nd if else")
            return isIn(char, aStr[:midChar])

print(isIn('r', 'r'))