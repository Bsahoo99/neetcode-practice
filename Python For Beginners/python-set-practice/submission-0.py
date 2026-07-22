from typing import List

def contains_duplicate(words: List[str]) -> bool:
    x = len(words)
    my_set = set(words)
    y = len(my_set)
    if x != y:
        return True
    else:
        return False    

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
