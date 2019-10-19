side1 = float(input("What is the lenght of your first side? "))
side2 = float(input("What is the lenght of your second side? "))
side3 = float(input("What is the lenght of your third side? "))

if ((side1 <= 0) or (side2 <= 0) or (side3 <= 0)):
    result = "Not a triangle"
else:
    if side1 == side2 == side3:
        result = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        result = "Isosceles"
    else:
        result = "Scalene"   