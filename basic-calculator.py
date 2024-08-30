def addition():
    result = number_1 + number_2
    print("The answer is " + str(result))

def subtraction():
    result = number_1 - number_2
    print("The answer is " + str(result))

def multiplication():
    result = number_1 * number_2
    print("The answer is " + str(result))

def division():
    result = number_1 / number_2
    print("The answer is " + str(result))

calculator_instruction = ["addition", "subtraction", "multiplication", "division"]




print("This calculator can perform: " + str(calculator_instruction))
make_operartion = input("do you want to make an operation? ")
while make_operartion == "yes":  
    
    number_1 = int(input("enter a number "))
    number_2 = int(input("enter an other number "))
    index = len(calculator_instruction)

    list_of_operations_types = ["+", "-", "*", "/" ]
    for i, operation in enumerate(list_of_operations_types):
        i += 1
        print(str(i) + ". " + operation)
    chosen_operation = int(input("enter the operation type (choose a number please) "))

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
    