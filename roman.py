converter = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10, 
    'V': 5,
    'I': 1,
}

def roman_to_arabic(numeral):
    total = 0
    for digit in numeral:
        if digit not in converter:
            raise ValueError('Bad Roman digit!')
        total += converter[digit]

    return total
