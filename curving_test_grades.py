import numpy as np

CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])

def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change

    # Increase scores, but don't allow them to go above 100.
    return np.clip(new_grades, grades, 100)

curvedGrades = curve(grades)
print(curvedGrades)
# [  91.25   54.25   83.25  100.     70.25  100.     93.25   31.25]