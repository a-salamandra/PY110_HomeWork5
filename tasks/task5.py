def task5(text:str) -> str:

    middle_point = len(text) // 2

    beginning_char = text[:middle_point]
    middle_char = text[middle_point] if len(text)%2 == 1 else ""
    end_char = text[middle_point+1:] if len(text)%2 == 1 else text[middle_point:]

    return f"{beginning_char[::-1]}{middle_char}{end_char[::-1]}"
