#!python

import string
import math

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """

    decimal = 0
    numbers = getIntList(str_num)

    for i in range(0, len(numbers)):
        power = len(numbers) - 1 - i
        decimal += numbers[i] * math.pow(base, power)

    return decimal


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """

    remainder = num
    largestIndex = None
    number_position = {}

    while (remainder != 0):
        # Determine what power to raise the base to
        power = int(math.floor(math.log(remainder, base)))
        # Determine what number goes at the position of the power
        index_number = int(math.floor(remainder / math.pow(base, power)))

        number_position[power] = convertNumberToLetter(index_number)

        remainder -= index_number * math.pow(base, power)

        if (largestIndex is None):
            largestIndex = power

    str_num = ""
    for i in reversed(range(0, largestIndex + 1)):
        if (i in number_position):
            str_num += str(number_position[i])
        else:
            str_num += "0"

    return str_num

# TODO: Write more efficient encode and decode functions
def efficient_encode(num, base):

    remainder = num
    encodedNum = ""

    while remainder is not 0:
        right_num = remainder % base
        right_char = convertLetterToNumber(right_num)
        encodedNum =  right_char + encodedNum

    return encodedNum


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """

    base10rep = decode(str_num, base1)

    return encode(base10rep, base2)



def getIntList(str_num):
    if (isNumber(str_num)):
        return [int(x) for x in str_num]

    ints = []
    for char in str_num:
        if(isNumber(char)):
            ints.append(int(char))
        else:
            ints.append(convertLetterToNumber(char))

    return ints

def convertLetterToNumber(letter):
    if (not letter.isalpha() or len(letter) != 1):
        raise ValueError

    distanceFromA = ord(letter.lower()) - 97

    return distanceFromA + 10

def convertNumberToLetter(num):
    if (num < 10):
        return str(num)

    #Offset by the characters that do exitst
    amountOver9 = num - 10

    return chr(amountOver9 + 97)

def isNumber(str_num):
    try:
        int(str_num)
        return True
    except:
        return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
