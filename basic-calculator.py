SIDE_BORDER_TEXTURE = "***"
TOP_BORDER_TEXTURE = "*"
WIDTH = 150

def print_calculator_instructions():
    text_to_print = "welcome to my calculator!"
    centerised_custom_printer(text_to_print)
    text_to_print = "This calculator can perform: addition, subtraction, multiplication, division"
    centerised_custom_printer(text_to_print)
    
def addition(number_1:int, number_2:int):
    result = number_1 + number_2
    return result

def subtraction(number_1:int, number_2:int):
    result = number_1 - number_2
    return result

def multiplication(number_1:int, number_2:int):
    result = number_1 * number_2
    return result

def division(number_1:int, number_2:int):
    result = number_1 / number_2
    return result

def centerised_custom_printer(text_to_print) :
    text = text_to_print if len(text_to_print) %2 == 0 else text_to_print + " " 
    width = 150
    space = " " 
    width_space = (width - len(text))/2 - len(SIDE_BORDER_TEXTURE) 
    padding = space * int(width_space)
    line_2 = SIDE_BORDER_TEXTURE + padding + text + padding + SIDE_BORDER_TEXTURE
    print(line_2)
    return padding

print("\n")
for i in range(2):
    print(TOP_BORDER_TEXTURE * WIDTH)
centerised_custom_printer(" ")
print_calculator_instructions()
centerised_custom_printer(" ")
print(TOP_BORDER_TEXTURE * WIDTH)

request_padding = centerised_custom_printer("do you want to make an operation?")
response_prompt = "response: "
make_operartion = input(SIDE_BORDER_TEXTURE + request_padding + response_prompt)

while make_operartion == "yes":  
    request_padding = centerised_custom_printer("enter number 1")
    number_1 = int(input(SIDE_BORDER_TEXTURE + request_padding + response_prompt))
    centerised_custom_printer("enter number 2")
    number_2 = int(input(SIDE_BORDER_TEXTURE + request_padding + response_prompt))

    list_of_operations_types = ["+", "-", "*", "/" ]
    for i, operation in enumerate(list_of_operations_types):
        i += 1
        centerised_custom_printer(str(i) + ". " + operation)
    centerised_custom_printer("enter the operation type (choose a number please) ")
    chosen_operation = int(input(SIDE_BORDER_TEXTURE + request_padding + response_prompt))

    if chosen_operation == 1:
        result = addition(number_1, number_2)
        centerised_custom_printer("The answer is " + str(result))
    elif chosen_operation == 2:
        centerised_custom_printer("The answer is " + str(subtraction(number_1, number_2)))
    elif chosen_operation == 3:
        centerised_custom_printer("The answer is " + str(multiplication(number_1, number_2)))
    elif chosen_operation == 4:
        if number_2 != 0:
            centerised_custom_printer("The answer is " + str(division(number_1, number_2)))
        else:
            centerised_custom_printer("division by zero is not possible!")
    else:
        centerised_custom_printer("This operation does not exist")
    request_padding = centerised_custom_printer("do you want to make an operation? ")
    make_operartion = input(SIDE_BORDER_TEXTURE + request_padding + response_prompt)
    while make_operartion != "no" and make_operartion != "yes":
        centerised_custom_printer("invalid response")
        request_padding = centerised_custom_printer("do you want to make an operation? ")
        make_operartion = input(SIDE_BORDER_TEXTURE + request_padding + response_prompt)

print(TOP_BORDER_TEXTURE * WIDTH)   
else:
    centerised_custom_printer("see you next time")
for i in range(2):
    print(TOP_BORDER_TEXTURE * WIDTH)
    