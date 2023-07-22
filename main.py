import json

# Cesar code

def cesarCode(txt, key):
    with open("products.json", 'r') as file:
        alphabetData = json.load(file)
    codeInNumber = []
    for letter in txt:
        for l in alphabetData:
            if alphabetData[f"{l}"] == letter.lower():
                codeInNumber.append(int(l) + int(key))

    codeWord = ''
    for num in codeInNumber:
        if num <= 26:
            codeWord += alphabetData[f"{num}"]
        else:
            codeWord += alphabetData[f"{num - 26}"]
    return codeWord.capitalize()

def antiCesarCode(txt, key):
    with open("products.json", 'r') as file:
        alphabetData = json.load(file)
    codeInNumber = []
    for letter in txt:
        for l in alphabetData:
            if alphabetData[f"{l}"] == letter.lower():
                codeInNumber.append(int(l) - int(key))

    codeWord = ''
    for num in codeInNumber:
        if num <= 0:
            codeWord += alphabetData[f"{26 + num}"]
        else:
            codeWord += alphabetData[f"{num}"]
    return codeWord.capitalize()


if __name__ == "__main__":
    # enterArr = [5, 2, 4, 8]

    word = "Python"
    print(cesarCode(word, 3))
    wordOne = "Sbwkrq"
    print(antiCesarCode(wordOne, 3))


# --------------------------------------------------------------------------------------

# MyStat Tasks

# def textPrinter ():
#     print("Don't compare yourself with anyone in this world…", "\n",
#           "if you do so, you are insulting yourself.", "\n",
#           "Bill Gates")

# def isPair (numOne, numTwo):
#     for nums in range(numOne, numTwo+1):
#         if nums%2==0:
#             print(nums)


# def squarePrinter (length, symbol):
#     arrX = []
#     arrY = []
#     for i in range(0, length):
#         arrY.append(symbol)
#     for j in range(0, length):
#         arrX.append(arrY)
#     for row in arrX:
#         for col in row:
#             print(col, end=" ")
#         print()


# def minFromFiveNum (one, two, three, four, five):
#     arr = []
#     arr.append(one)
#     arr.append(two)
#     arr.append(three)
#     arr.append(four)
#     arr.append(five)
#     arr.sort()
#     print(arr[0])


# def multOfNumbers(rangeStart, rangeEnd):
#     result = 1
#     if rangeStart>rangeEnd:
#         temp = rangeStart
#         rangeStart=rangeEnd
#         rangeEnd=temp
#     for i in range(rangeStart,rangeEnd+1):
#         result *=i
#         print(result)


# def quantityOfNumbers(number):
#     print(len(number))


# def isPalindrome (number):
#     if number == number[::-1]:
#         return True
#     else:
#         return False

# if __name__ == "__main__":





