if __name__ == "__main__":

    # # Test 1
    # numberOne = int(input("Enter first number: "))
    # numberTwo = int(input("Enter second number: "))
    # numberThree = int(input("Enter third number: "))
    #
    # sum = numberOne + numberTwo + numberThree
    # multiply = numberOne * numberTwo * numberThree
    #
    # ask = input("Sum or Multiply?\n"
    #             "S or M: ")
    #
    # if (ask == "S"):
    #     print("The sum is: ", sum)
    # else:
    #     print("The multiply is ", multiply)

    # # Test 2
    #
    # numberOne = int(input("Enter first number: "))
    # numberTwo = int(input("Enter second number: "))
    # numberThree = int(input("Enter third number: "))
    #
    # ask = input("Maximum, minimum or average?\n"
    #             "Max, Min or Ave: ")
    #
    # list = [numberOne, numberTwo, numberThree]
    # list.sort()
    #
    # min = list[0]
    # max = list[2]
    # average = round((numberOne + numberTwo + numberThree)/3)
    #
    # if (ask=="Max"):
    #     print(max)
    # elif (ask=="Min"):
    #     print(min)
    # else:
    #     print(average)

    # Test 3
    meters = float(input("Enter the meters: "))
    choose = input("What to convert meters into?\n"
                   "m - miles\n"
                   "i - inches\n"
                   "y - yards\n"
                   "Your choose: ")

    convertToMiles = 0.00062137*meters
    convertToInches = 39.370*meters
    convertToYards = 1.0936*meters

    if (choose == "m"):
        print(meters, "meters = ", convertToMiles, "miles")
    elif (choose == "i"):
        print(meters, "meters = ", convertToInches, "inches")
    else:
        print(meters, "meters = ", convertToYards, "yards")