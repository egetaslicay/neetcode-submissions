from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = {} 
    for element in word: 
        if(element in my_dict): 
            my_dict[element] += 1
        else: 
            my_dict[element] = 1
    
    return my_dict



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
