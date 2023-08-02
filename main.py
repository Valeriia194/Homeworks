# TG Bot

# import telebot
# from telebot import types
#
# bot = telebot.TeleBot("")
#
# print("______ START BOT ______")
#
# def simple_numbers(star_value, end_value):
#     simple_num = []
#     for i in range(star_value, end_value):
#         flag = True
#         for dil in range(star_value, end_value):
#             if dil != 1 and dil < i:
#                 result = i % dil
#                 if result == 0:
#                      flag = False
#                      break
#             if dil >= i:
#                 break
#         if flag:
#           simple_num.append(i)
#     return simple_num
#
# def main_reply_menu():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # itembtn1 = types.KeyboardButton('a')
#     # itembtn2 = types.KeyboardButton('v')
#     # itembtn3 = types.KeyboardButton('d')
#     # markup.add(itembtn1, itembtn2, itembtn3)
#     markup.row(types.KeyboardButton("$"), types.KeyboardButton("/start"), types.KeyboardButton("€"))
#     markup.row(types.KeyboardButton("🦆Simple numbers"))
#     return markup
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(msg):
#     # bot.reply_to(message, "Howdy, how are you doing?")
#     cid = msg.chat.id
#     bot.send_message(cid, "Hello!", reply_markup=main_reply_menu())
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(msg):
#     # bot.reply_to(message, message.text)
#     cid = msg.chat.id
#     if msg.text == "🦆Simple numbers":
#         numbers = simple_numbers(1,100)
#         tempText = "List of simple numbers: \n\n"
#         for num in numbers:
#             tempText+=f"{num}"
#         bot.send_message(cid, tempText)
#     elif msg.text == "€":
#         cid = msg.chat.id
#         bot.send_message(cid, "Current course of Euro is: 40.53")
#     elif msg.text == "$":
#             cid = msg.chat.id
#             bot.send_message(cid, "Current course of Dollar is: 36.95")
#
# bot.infinity_polling()

# Task 1, 2

# def factorial (number):
#     if number<0:
#         print("Wrong number, try again!")
#     else:
#         fact = 1
#         for i in range (2, number+1):
#             fact=fact*i
#         print(fact)

# Task 3,4

def addListOfNums (numberArr):
    num = 5
    print("Enter 5 numbers: ")
    while (num>0):
        numberArr.append(int(input()))
        num-=1

def menu (numberArr):
    print(f"Choose your action: ", "\n",
          "Print list(1)", "\n",
          "Max value(2)", "\n",
          "Min value(3) ", "\n",
          "Show element by index(4)", "\n",
          "Delete element by index(5)", "\n",
          "Exit(0)", "\n",)
    choose = int(input("Your choose: "))
    tempArr = numberArr.copy()
    if (choose == 1):
        print(numberArr)
        menu(numberArr)
    elif (choose == 2):
        tempArr.sort()
        print(tempArr[-1])
        menu(numberArr)
    elif (choose == 3):
        tempArr.sort()
        print(tempArr[0])
        menu(numberArr)
    elif (choose ==4):
        i = int(input("Enter the index: "))
        if (i > 0 and i < len(numberArr) - 1):
            print(numberArr[i-1])
        else:
            print("Wrong index!")
        menu(numberArr)
    elif (choose == 5):
        i = int(input("Enter the index: "))
        if (i>0 and i<len(numberArr)-1):
           numberArr.pop(i-1)
           print("New array is: ", numberArr)
        else:
            print("Wrong index!")
        menu(numberArr)
    elif (choose == 0):
        print("Good bye!")
    else:
        print("Wrong choice, try again!")
        menu(numberArr)

if __name__ == "__main__":
    # number = int(input("Enter the number for find factorial: "))
    # factorial(number)

    newArr = []
    addListOfNums(newArr)
    menu(newArr)
