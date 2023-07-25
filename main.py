def multiply (someArr):
    result = 1
    for i in range(len(someArr)):
        result *= someArr[i]
    print("The multiply is: ", result)

def minimum (someArr):
    tempArr = sorted(someArr)
    print("The lowest number is: ", tempArr[len(tempArr)-1])

def simpleNums(someArr):
    howMuch = 0
    for i in range(len(someArr)):
        if someArr[i]%3!=0 and someArr[i]%2!=0:
            howMuch+=1
    print("Here is ", howMuch, "simple numbers")

if __name__ == "__main__":
    arrOfNums = [2, 17, 4, 23, 8, 13]
    multiply(arrOfNums)
    minimum(arrOfNums)
    simpleNums(arrOfNums)
