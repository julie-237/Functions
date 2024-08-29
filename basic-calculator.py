print("This calculator can perform: addition, subtraction, multiplication and division")
number_1 = input("enter a number")
number_2 = input("enter an other number")

list_of_operations_types = ["+", "-", "*", "/" ]
for i, operation in enumerate(list_of_operations_types):
    i += 1
    print(str(i) + "." + operation)
chosen_operation = int(input("enter the operation type (choose a number please)"))

