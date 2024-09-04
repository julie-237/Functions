def get_grade_list_from_user():
    usergrade = get_grade_from_user()
    while usergrade != -1:
        if usergrade >= 0 and usergrade <= 10:
            grade_list.append(usergrade)
            usergrade = get_grade_from_user()
        else:
            print("invalid grade")
            usergrade = get_grade_from_user()
    return grade_list

def get_grade_from_user():
    return int(input("give a grade "))
    

def compute_grade_list_minimum(grade_list: list[int]):
    minimum_grade = grade_list[0]
    for  grade in grade_list:
        if grade < minimum_grade:
            minimum_grade = grade
    return minimum_grade

def compute_grade_list_maximum(grade_list: list[int]):
    maximum_grade = grade_list[0]
    for  grade in grade_list:
        if grade > maximum_grade:
            maximum_grade = grade
    return maximum_grade

def compute_grade_list_average(grade_list: list[int]):
    total_grades = sum_of_grade_list(grade_list)
    average = total_grades / len(grade_list)
    return average
    
def sum_of_grade_list(grade_list: list[int]):
    sum = 0
    for n in grade_list:
       sum += n
    return sum
    

grade_list = []

print("Welcome to grade statistics")
grade_list = get_grade_list_from_user()
if len(grade_list) > 0:
    print("you have " + str(len(grade_list)) + " grades, which are " + str(grade_list))
    least_grade = compute_grade_list_minimum(grade_list)
    highest_grade = compute_grade_list_maximum(grade_list)
    average_grade = compute_grade_list_average(grade_list)
    print("min grade is " + str(least_grade) + ", " + "max grade is " + str(highest_grade) + ", " + "the average is " + str(average_grade))
else:
    exit   
