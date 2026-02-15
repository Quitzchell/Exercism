def equilateral(sides):
    return triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return triangle(sides) and len(set(sides)) == 3
    
def triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c
