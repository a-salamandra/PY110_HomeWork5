def find_word(str_:str) -> str:

    str_ = str_.split()
    words = {}
    for word in str_:
        sum_ = 0
        for char in word:
            if char.isalpha():
                sum_ += ord(char)
        words[word] = sum_
    return max(words,key=words.get)
