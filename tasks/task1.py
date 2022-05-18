def task1(binary_number: list) -> int:
    str_ = "".join([str(i) for i in binary_number])
    return int(str_,base=2)