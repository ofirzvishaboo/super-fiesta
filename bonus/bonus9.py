password = input("Enter your password: ")

result = {}
if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Numbers"] = digit
upper = False
for i in password:
    if i.isupper():
        upper = True
result["Upper-case"] = upper
print(result)

if all(result.values()):  
    print("nice password")
else:
    print("FU")