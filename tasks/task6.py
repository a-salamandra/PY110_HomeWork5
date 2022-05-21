def roman_to_int(rn:str) -> int:

    result = 0
    romannums = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    for index in range(len(rn)):
        if index < len(rn)-1:
            if romannums[rn[index]] < romannums[rn[index+1]]:
                result -= romannums[rn[index]]
            else:
                result += romannums[rn[index]]

    result += romannums[rn[-1]]
    return result

