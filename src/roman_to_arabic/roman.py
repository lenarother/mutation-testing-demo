ROMAN = 'IVXLCDM'
ARABIC = (1, 5, 10, 50, 100, 500, 1000)
ROMAN_ARABIC_MAP = dict(zip(ROMAN, ARABIC))


def get_current_roman(i, previous):
    value = ROMAN_ARABIC_MAP.get(i)
    return -value if value < previous else value


def roman2arabic(roman):
    previous = 0
    arabic = 0
    for i in roman[::-1]:
        value = get_current_roman(i, previous)
        arabic += value
        previous = abs(value)
    return arabic
