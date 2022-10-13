def int_to_roman(num):
    # Storing roman values of digits from 0-9

    #thousands place
    m = ["", "M", "MM", "MMM"]

    #hundreds place
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]

    #tens place
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]

    #ones place
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundreds +
           tens + ones)

    return ans

  print(int_to_roman(666))
