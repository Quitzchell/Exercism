def leap_year(year):
    divisible_by_four = year % 4 is 0
    divisible_by_hundred = year % 100 is 0
    divisible_by_four_hundred = year % 400 is 0

    if divisible_by_four and divisible_by_hundred:
        if divisible_by_four_hundred:
            return True
        else: 
            return False
    elif divisible_by_four:
        return True
    
    return False
            
            