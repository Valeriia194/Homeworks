if __name__ == "__main__":

    # # Task 1
    #
    # DayOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # flag = True
    #
    # while flag:
    #     day = int(input("Enter the number of day (from 1 to 7): "))
    #     if 0 <= day <= 7:
    #         print("It's ", DayOfWeek[day - 1])
    #         flag = False
    #     else:
    #         print("Wrong number, try again!")


    # # Task 2
    #
    # months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
    #           'October', 'November', 'December']
    # flag = True
    #
    # while flag:
    #     monthNum = int(input("Enter the number of month (from 1 to 12): "))
    #     if 0 <= monthNum <= 12:
    #         print("It's ", months[monthNum - 1])
    #         flag = False
    #     else:
    #         print("Wrong number, try again!")


    # # Task 3
    #
    # num = int(input("Enter the number: "))
    # if num > 0:
    #     print("The number is positive!")
    # elif num < 0:
    #     print("The number is negative!")
    # else:
    #     print("The number is equal zero!")


    # #Task 4
    #
    # numOne = int(input("Enter first number: "))
    # numTwo = int(input("Enter second number: "))
    #
    # if numOne == numTwo:
    #     print("It's equal!")
    # else:
    #     if numOne > numTwo:
    #         print("Not equal!\n", numOne, numTwo)
    #     else:
    #         print("Not equal!\n", numTwo, numOne)


    # Task 5 (Class Task)

    products = {
        'apples': 10,
        'bananas': 15,
        'oranges': 12,
        'pears': 8,
        'kiwi': 20
    }

    balance = 100

    shopping_cart = []

    while balance > 0:

        for product in products:
            print(product, products[product])

        choice = input("What do you want to buy? Or type \"q\" if you want to quit\n")

        if choice == "q":
            break

        if choice in products:
            if balance >= products[choice]:
                shopping_cart.append(choice)
                print(choice, "is added to your shopping cart")
                balance -= products[choice]
            else:
                print("You don't have enough money to buy it :(")
        else:
            print("Not find your choice!")

    print("You bought:")
    shopping_cart_sum = 0
    for product in shopping_cart:
        shopping_cart_sum += products[product]
        print(product)

    print("Your shopping cart sum is:", shopping_cart_sum)
    print("Your current balance is:", balance)