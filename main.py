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

# def delNum(someArr, temp):
#     print(someArr)
#     num = int(input("Enter the number to delete: "))
#     for i in someArr:
#         if i==num:
#             someArr.remove(num)
#             temp += 1
#     a = int(input("One more delete?(1-Yes,2-No) "))
#     if a == 1:
#         delNum(someArr, temp)
#     else:
#         print("You have deleted ", temp, "numbers.")

def compareArrs(arrOne, arrTwo):
    newArr = []
    for i in arrOne:
        for j in arrTwo:
            if i==j:
                newArr.append(j)
    print(newArr)

def degreeOfNum():
    newArr = []
    tempNum= 1
    print("Enter 5 numbers for list by enter: ", "\n")
    for i in range (0, 5):
        a = int(input())
        tempNum=a*a
        newArr.append(tempNum)
    print(newArr)

if __name__ == "__main__":
    arrOfNums = [2, 17, 4, 23, 8, 13, 5, 6]
    arrOfNumsTwo = [1, 5, 3, 23, 8, 4, 2, 1]
    multiply(arrOfNums)
    minimum(arrOfNums)
    simpleNums(arrOfNums)

    # quantityOfDel = 0
    # delNum(arrOfNums, quantityOfDel)

    compareArrs(arrOfNums, arrOfNumsTwo)
    degreeOfNum()


