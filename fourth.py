

# class Cat:
#     name = ""
#     my_color = ""
#     def __init__(self):
#         p
#     def dont_swim(self):
#         print("cats")
#     def cat_swim(self):
#         print("cats dont like to swim")
#
# with open("todos1.txt", "w") as file:
#     file.write("dsgttgrrtgrthrthrt")
#
# with open("todos1.txt", "r") as file:
#     my_file = file.read()
#     print(my_file)
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def howl(self):
        print("ahoooo")

class Huski_Dog(Dog):
    def __init__(self, name, age, breed):
        Dog.__init__(self, name, age)
        self.breed = breed
class black_huski(Dog):
    def __init__(self, name, age, breed):
        Dog.__init__(self, name, age, breed)

    def return_color(self):
        return "black"

def main():
    sam = Huski_Dog("rexi", 9, "chizu")
    sam1 = Huski_Dog("lulu", 1, "huski")
    sam2 = Huski_Dog("momo", 11, "shark")
    dog_list = [sam, sam1, sam2]
    for i in dog_list:
        print(i.name)
        print(i.age)
        print(i.breed)
    # print(sam.age)
    # print(sam.breed)


main()
