
SIDE_BORDER_TEXTURE = "***"
TOP_BORDER_TEXTURE = "*"
WIDTH = 150
SPACE = " " 
RESPONSE_PROMPT = "response: "

def centerised_custom_printer(text_to_print) :
    text = text_to_print if len(text_to_print) %2 == 0 else text_to_print + " " 
    width_space = (WIDTH - len(text))/2 - len(SIDE_BORDER_TEXTURE) 
    padding = SPACE * int(width_space)
    line_2 = SIDE_BORDER_TEXTURE + padding + text + padding + SIDE_BORDER_TEXTURE
    print(line_2)
    return padding

def get_grade_list_from_user():
    usergrade = get_grade_from_user()
    while usergrade != -1:
        if usergrade >= 0 and usergrade <= 10:
            grade_list.append(usergrade)
            usergrade = get_grade_from_user()
        else:
            centerised_custom_printer("invalid grade")
            usergrade = get_grade_from_user()
    return grade_list

def get_grade_from_user():
    grade = centerised_custom_printer("give a grade ")
    return int(input(SIDE_BORDER_TEXTURE + grade + RESPONSE_PROMPT))
    

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
print("\n")
for i in range(2):
    print(TOP_BORDER_TEXTURE * WIDTH)
    centerised_custom_printer(" ")
centerised_custom_printer("Welcome to grade statistics")
centerised_custom_printer(" ")
print(TOP_BORDER_TEXTURE * WIDTH)
grade_list = get_grade_list_from_user()
if len(grade_list) > 0:
    centerised_custom_printer("you have " + str(len(grade_list)) + " grades, which are " + str(grade_list))
    least_grade = compute_grade_list_minimum(grade_list)
    highest_grade = compute_grade_list_maximum(grade_list)
    average_grade = compute_grade_list_average(grade_list)
    print(TOP_BORDER_TEXTURE * WIDTH)
    centerised_custom_printer("min grade is " + str(least_grade) + ", " + "max grade is " + str(highest_grade) + ", " + "the average is " + str(average_grade))
    for i in range(2):
        print(TOP_BORDER_TEXTURE * WIDTH)
else:
    exit   
