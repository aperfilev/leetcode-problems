
with open('file.txt', 'r') as file:
    for i in range(9):
        file.readline()

print(file.readline())

file.close()
