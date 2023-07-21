#!/usr/bin/env python3

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")

# // JavaScript
# let dog = "cuddly";
# let owner;

# switch (dog) {
#   case "hungry":
#     owner = "Refilling food bowl.";
#     break;
#   case "thirsty":
#     owner = "Refilling water bowl.";
#     break;
#   case "playful":
#     owner = "Playing tug-of-war.";
#     break;
#   case "cuddly":
#     owner = "Snuggling.";
#     break;
#   default:
#     owner = "Reading newspaper.";
#     break;
# }

# # Python
# dog = "cuddly"

# if dog == "hungry":
#     owner = "Refilling food bowl."
# elif dog == "thirsty":
#     owner = "Refilling water bowl."
# elif dog == "playful":
#     owner = "Playing tug-of-war."
# elif dog == "cuddly":
#     owner = "Snuggling."
# else:
#     owner = "Reading newspaper."


# dog = "cuddly"

# dict_map = {
#     "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")

def admin_login(username, password):
    # your code here
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None
