def classify_triangle(ang1, ang2, ang3):
    if ang1 == ang2 == ang3 == 60:
        return "Equilateral"
    elif ang1 + ang2 + ang3 == 180:
        if ang1 == ang2 or ang1 == ang3 or ang2 == ang3:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Error"

ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

result = classify_triangle(ang1, ang2, ang3)
print(result)