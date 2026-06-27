from typing import List

def read_integers() -> List[int]:
    number_string = input()
    myStringList = number_string.split(",")
    res = []
    for element in myStringList: 
        res.append(int(element))

    return res
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
