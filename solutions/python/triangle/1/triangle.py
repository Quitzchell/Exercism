def equilateral(sides):
    if not triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    return triangle(sides) and not equilateral(sides) and not isosceles(sides)
    
def triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c
