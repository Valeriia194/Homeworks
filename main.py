# Task 1, 2
def yourName():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age > 0 and age < 130:
        print(" Hello ", name, "\n", "Your age is ", age)
    else:
        print("Wrong age! Try again!")
        yourName()

# Task 3, 4
def numbersAdd():
    print("Enter 5 positive numbers: ")
    arrNum = []
    result = 0
    for i in range(5):
        a = int(input(""))
        arrNum.append(a)
    for i in arrNum:
        if i < 0:
            print("U enter negative number, try again!")
            numbersAdd()
        else:
            result += i
    print("The sum of all numbers is: ", result)


if __name__ == "__main__":
    numbersAdd()
