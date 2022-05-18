def wave(text):
    text = list(text)

    for i in range(len(text)):
        text[i] = text[i].upper()
        yield "".join(text)
        text[i] = text[i].lower()
