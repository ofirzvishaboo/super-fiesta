def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    
    value = data[1:]
    value = [float(i) for i in value]

    avg = sum(value) / len(value)
    return avg
    

average = get_average()
print(average)