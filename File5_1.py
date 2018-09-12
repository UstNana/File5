# -*- coding: utf-8 -*-
#file = open("txt.txt")
#file_py = file.read().split("\n")[:-1]


dict_2 = {}
dict_1 = {}
with open("txt.txt") as file:
    for i, line in enumerate(file):
        if i == 1:
              for headline in file:
                key_1 = headline.split(" ")[0]
                dict_1[key_1] = dict_2
        if i == 2:
            for headline in file:
                key = headline.split("")[0]
                value = headline.split(" ")[1:]
                dict_2[key] = value

print(dict_1)
file.close()