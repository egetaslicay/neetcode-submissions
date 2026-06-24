def remove_fourth_character(word: str) -> str:
    first_four = word[:3]
    after_four = word[4:]
    return first_four + after_four


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
