
file = open("file.txt")
file1 = file.read().split("\n")[:-1]

dict = dict()

for line in file1:
    key = line.split(" ")[0]
    key = dict()
    for element in line:
      key1 = line.split(" ")[0]
      value = line.split(" ")[1:]
      dict[key1] = value

file.close()
