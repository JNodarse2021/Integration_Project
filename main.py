# Name: Jose Nodarse
# Description: My program is a combination of everything that I have learned so far in the class.

import math
def get_square_root(a,b):
    cube_plus_1 = a**3 + b**3 + 1
    square_root = math.sqrt(cube_plus_1)
    return square_root

def diameter(radius):
    diameter = (radius * 2)
    return diameter

def area(radius):
    area = math.pi * radius ** 2
    return area

def get_smaller(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    return smaller

def good_input():
    got_good_input = False
    while got_good_input == False:
      try:
        x = int(input("Please enter a whole number: "))
        got_good_input = True
      except ValueError:
        print("That was not a a whole number. Please try again.")

    good = "Valid"
    return good

def average():
    num1 = int(input("Enter number: "))
    sum2 = 0
    divisor = 0
    while num1 != 0:
        sum2 = sum2 + num1
        divisor = divisor + 1
        num1 = int(input())
    else:
        average1 = (sum2 / divisor)
    return average1

def sum():
    total = 0
    for x in range(5):
        number = int(input("Enter a number: "))
        total += number
    sum1 = total
    return sum1

def Boo_op():# Boolean Operator "and", "or", "not"
    weight = input("Enter weight(less than 10): ")
    cost = input("Enter cost(less than or equal to 20): ")
    num1 = float(weight)
    num2 = float(cost)
    if num1 < 10 and num2 <= 20:
        boo_op = "Valid"
    elif num1 < 10 or num2 <= 20:
        boo_op = "Partially Valid"
    else: # not(num1 < 10 and/or num2 <= 20)
        boo_op = "Completely Invalid"
    output = boo_op
    return output

def main():
    # greeting/ introduction to the user
    print("Hello, my name is Jose Nodarse\n")
    user_first_name = input("What is your first name? ")
    user_last_name = input("What is your last name? ")
    print("Nice to meet you,", user_first_name, user_last_name)
    print("This will be a simple program.\nHopefully it does not bore you to death.\n")

    # Menu
    menu_options = True
    while menu_options:
        print("Enter the choice for what you would like to see")
        print("1.")
        print("2.")
        print("3.")
        print("4.")
        print("5. Quit")
        pick_option = int(input())

        if pick_option == 1:
            first_favorite_word = input("What word do you like enough to see it repeated 20 times: ")
            second_favorite_word = input("What other word do you like enough to see it repeated 20 times: ")

            # *: This string operator repeats the same word the indicated number of times.
            print(first_favorite_word * 20)
            print(second_favorite_word * 20)
            print(" ")
            # +: This string operator concatenates or combines words.
            print("Lets see how they look together:", first_favorite_word + second_favorite_word)
            print("It probably looks off right?\nSome words are not meant to go together.\n")

        elif pick_option == 2:
            first_number = input("Enter first number: ")
            second_number = input("Enter second number: ")
            third_number = input("Enter third number: ")
            fourth_number = input("Enter fourth number: ")
            fifth_number = input("Enter fifth number: ")
            sixth_number = input("Enter sixth number: ")
            seventh_number = input("Enter seventh number: ")
            num1 = int(first_number)
            num2 = int(second_number)
            num3 = int(third_number)
            num4 = int(fourth_number)
            num5 = int(fifth_number)
            num6 = int(sixth_number)
            num7 = int(seventh_number)

            # basic calculations(**, *, /, %, //, +, -)

            # **: This numeric operator raises numbers to a power.
            print("num1 ** num3 =", num1 ** num3)

            # *: This numeric operator multiplies numbers together.
            print("num2 * num5 =", num2 * num5)

            # /: This numeric operator divides numbers.
            print("num4 / num1 =", num4 / num1)

            # %: This numeric operator is called modulus and it gives the remainder after dividing two numbers.
            print("num3 % num2 =", num3 % num2)

            # //: This numeric operator divides numbers but only gives the integer as the output(does not round).
            print("num1 // num5 =", num1 // num5)

            # +: This numeric operator adds numbers together.
            print("num4 + num6 =", num4 + num6)

            # -: This numeric operator subtracts numbers.
            print("num6 - num7 =", num6 - num7)

            print(" ")
            print("Now to mix it up a little.\n")

            # Combined operations
            print("num2 + num6 * num3 - num4 =", (num2 + num6) * (num3 - num4))
            print("num1 + num2 / num3 - num4 =", (num1 + num2) / (num3 - num4))
            print("num6 % num5 ** num4 + num1 =", (num6 % num5) ** (num4 + num1))
            print("num1 / num6 % num7 * num2 =", format((num1 / num6) % (num7 * num2), "0.2f"))

            print(" ")

        elif pick_option == 3:
            print("Now lets do something slightly harder, at least for me since I am the one coding it\n")

            # Calculating and displaying the the total cost for chosen transport
            print("Imagine you are going traveling, but before you go some thinking needs to be done.\n")
            transport_type = input("Enter your favorite mode of transport(ex. airplane, train, etc.): ")
            number_tickets = int(input("Enter the number of tickets needed: "))
            transport_cost = float(input("Enter the cost of one ticket: "))
            total_cost = number_tickets * transport_cost
            print("Transport type:", transport_type)
            print("Cost of one ticket: $", format(transport_cost, ".2f"), sep='')
            print("Number of tickets bought:", number_tickets)
            print("Total cost: $", format(total_cost, ".2f"), sep='')

            print("Lets see if you can follow directions(PS: Don't follow directions)")
            print("The operation will repeat, the second will not")
            print(good_input())
            print(Boo_op())

            print("Lets find the average of a set of numbers")
            print("Enter any number you want, except 0. When you want to end, enter 0")
            print(format(average(), ".2f"))

            print("Finding the Sum of Five Numbers")
            print("The total is:", sum())

        elif pick_option == 4:
            # Finding the smaller number
            user_input1 = int(input("Enter a number: "))
            user_input2 = int(input("Enter a second number: "))

            smaller_number = get_smaller(user_input1, user_input2)
            print("The smaller number is:", smaller_number)

            # Get the square root of the cubes of 2 and 3 plus 1
            print("Now lets do some slightly more complicated math")
            print("Lets cube 2 and 3 then add one and take the square root")
            print("The square root of the squares of 2 and 3 plus 1 is:", get_square_root(2,3))

            # Getting the diameter and Area of a circle
            print("Now for some circle math")
            radius = int(input("Enter the radius: "))
            area1 = area(radius)
            diameter1 = diameter(radius)
            print("The area of the circle is:", format(area1, ".2f"))
            print("The diameter of the circle is:", format(diameter1, ".2f"))

        elif pick_option == 5:
            menu_options = False
        else:
            print("Invalid selection. Try again.")

    print(" ")
    # Using end=
    print("Well that is pretty much it for now.", end=" ")
    print("Hopefully it was somewhat interesting.")
    print("GOOD BYE :)")

main()