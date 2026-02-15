def is_armstrong_number(number):
    digits = str(number)
    length = len(digits)
    total = 0
    
    for digit in digits:
        total += int(digit)**length

    return total == number