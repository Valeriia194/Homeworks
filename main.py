if __name__ == "__main__":

    # # Task 1 + Task 2
    #
    # a = int(input("Enter the first number: "))
    # b = int(input("Enter the second number: "))
    # arr = []
    #
    # # All numbers
    # for i in range(a, b + 1):
    #     arr.append(i)
    # print(arr)
    #
    # # numbers vice versa
    # for i in range(len(arr)):
    #   arr[i:i+len(arr)] = sorted(arr[i:i+len(arr)], reverse = True)
    # print(arr)
    #
    # # numbers divided on 7
    # for i in range(a, b + 1):
    #     if i % 7 == 0:
    #         print(i)
    #
    # # how much divided on 5
    # fiveNumbers = 0
    # for i in range(a, b + 1):
    #     if i % 5 == 0:
    #         fiveNumbers+=1
    # print("Quantity of numbers divided on 5: ", fiveNumbers)


    # Task 3

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    for i in range(a, b + 1):
        if i % 3 == 0 and i%5!=0:
            print("Fizz")
        elif i % 5 == 0 and i%3!=0:
            print("Buzz")
        elif i % 5 == 0 and i%3==0:
            print("Fizz Buzz")
        else:
            print(i)