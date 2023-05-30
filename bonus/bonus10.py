try:
    width = float(input("Enter a rectangle width: "))
    length = float(input("Enter a rectangle length: "))
    if width == length:
        exit("That looks like a sqaure.")
    area = width * length
    print(area)
except ValueError:
    print("please enter a number.")