import mybonus as mybonus


feet_inches = input("Enter feet and inches: ")
parsed = mybonus.parse(feet_inches)
result = mybonus.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("midget")
else:
    print("ok")