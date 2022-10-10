list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def converter(num):
    answer = ''

    while num > 0:
        for int, rom in list:
            while num >= int:
                answer += rom
                num -= int

    return answer


# *enter your number to convert in the parentheses*
print(converter(3000))
