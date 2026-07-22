from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    x = 0
    for i in my_set:
        x += 1
    return x    


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
