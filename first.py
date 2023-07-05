from functions import USD, ILS
import time

now = time.strftime("%d  %b - %Y %H:%M:%S ")
print("It is", now)

# def should_stay():
#     user_dec = input("Do you want to do another calculation? y/n")
#     if user_dec == "y" or user_dec == "Y":
#         continue
#     elif user_dec == "n" or user_dec == "N":
#         break

def get_user_value():
    restart = True

    while restart:
        user_choice = input("1 - D to S / 2 - S to D: ")
        if user_choice == "1":
            value_to_convert = float(input("Enter quantity to convert: "))
            usd = USD()
            result = usd.calculate(value_to_convert)
            print(result)
            return result
        elif user_choice == "2":
            value_to_convert = float(input("Enter quantity to convert: "))
            ils = ILS()
            result = ils.calculate(value_to_convert)
            print(result)
            return result
        else:
            print("wrong input")
            continue

def main():
    restart = True
    mylist = []
    while restart:
        mylist.append(get_user_value())
        choice = input("Would you like to start over? y/n: ")
        if choice == "y":
            print(mylist)
            continue
        elif choice == "n":
            print(mylist)
            return mylist
        else:
            choice = input("Would you like to start over? y/n: ")



main()