def add_two_numbers() -> int:
    two_nums = input()
    myStringList = two_nums.split(",")
    lis = []
    for element in myStringList: 
        lis.append(int(element))

    sum = 0 
    for element in lis: 
        sum += element
    
    return sum 


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
