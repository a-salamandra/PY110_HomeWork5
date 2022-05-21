from itertools import cycle

def endless_wave(text:str, symbol:str) -> str:
    text = list(text)
    for index, char in cycle(enumerate(text)):
        if char != " ":
            text[index] = symbol
            yield "".join(text)
            text[index] = char
