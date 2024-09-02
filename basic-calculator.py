    
design_2 = "***" 
width = 150
space = " " 


def calculator_instructions():
    text_to_print = "welcome to my calculator!"
    border_design_2(text_to_print)
    text_to_print = "This calculator can perform: addition, subtraction, multiplication, division"
    border_design_2(text_to_print)

def addition():
    result = number_1 + number_2
    text_to_print = "The answer is " + str(result)
    border_design_2(text_to_print)

def subtraction():
    result = number_1 - number_2
    text_to_print = "The answer is " + str(result)
    border_design_2(text_to_print)

def multiplication():
    result = number_1 * number_2
    text_to_print = "The answer is " + str(result)
    border_design_2(text_to_print)

def division():
    result = number_1 / number_2
    text_to_print = "The answer is " + str(result)
    border_design_2(text_to_print)
    
def border_design_1():
    width = 150
    design_1 = "*" 
    line_1 = design_1 * width
    print(line_1)

def border_design_2(text_to_print) :
    width_space = (width - len(text_to_print))/2 - len(design_2) 
    spacing = space * int(width_space)
    line_2 = design_2 + spacing + text_to_print + spacing + design_2
    print(line_2)

def border_design_3(text_to_print):
    width_space = (width - len(text_to_print))/2 - len(design_2) 
    spacing = space * int(width_space)
    line_3 = design_2 + spacing 
    
    
   
print("\n")

border_design_1()
border_design_1()
border_design_2(" ")
calculator_instructions()
border_design_2(" ")
border_design_1()

  
text_to_print = "do you want to make an operation?"
border_design_2(text_to_print)

make_operartion = input(" ")
border_design_3(make_operartion)
while make_operartion == "yes":  
    text_to_print = "enter number 1 "
    border_design_2(text_to_print)
    number_1 = input(" ")
    border_design_3(number_1)
    text_to_print = "enter number 2"
    border_design_2(text_to_print)
    number_2 = input(" ")
    border_design_3(number_2)

    list_of_operations_types = ["+", "-", "*", "/" ]
    for i, operation in enumerate(list_of_operations_types):
        i += 1
        text_to_print = str(i) + ". " + operation
        border_design_2(text_to_print)
    text_to_print = "enter the operation type (choose a number please) "
    border_design_2(text_to_print)
    chosen_operation = int(input())
    border_design_3(chosen_operation)

    if chosen_operation == 1:
        addition()
    elif chosen_operation == 2:
        subtraction()
    elif chosen_operation == 3:
        multiplication()
    elif chosen_operation == 4:
        if number_2 != 0:
            division()
        else:
            print("division by zero is not possible!")
    else:
        print("This operation does not exist")
    make_operartion = input("do you want to make an operation? ")
    while make_operartion != "no" and make_operartion != "yes":
        print("invalid response")
        make_operartion = input("do you want to make an operation? ")
    
else: 
    print("see you next time")
    