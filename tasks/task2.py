def wave(text:str) -> None:

    text = list(text)

    for i in range(len(text)):
        if text[i] != " ":
            text[i] = text[i].upper()
            print("".join(text))
            text[i] = text[i].lower()

