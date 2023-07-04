import datetime

with open("todos.txt", 'a') as file:
    file.writelines("ok" + '\n')

with open("todos.txt", 'r', encoding='utf=8') as file:
    mm = file.read()
    print(mm)

print(datetime.datetime.now())
