###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >=14:
        grade='good'
    elif points >=10:
        grade='satisfactory'
    else:
        grade='fail'
    return grade


test_result = 15
final_grade = pts_to_grade(test_result)
print(final_grade)