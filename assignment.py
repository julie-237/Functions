
def sum_of_two_numbers(number_1 : int, number_2: int):
    sum = number_1 + number_2
    print("the sum of " + str(number_1) + "and" + str(number_2) + "is" + str(sum))

def sum_of_single_natural_numbers(n: int):
    #sum = (n*(n+1)) /2
    #print(sum)
    sum = 0
    for n in range(0, 10):
        sum += 0
        print(sum)
        
    
def sum_of_number_list(number_list: list[int]):
    sum = 0
    for n in number_list:
       sum += n
    return sum
def print_sum_of_number_list(number_list: list[int]):
    sum = sum_of_number_list(number_list)
    if len(number_list) >= 2:
        number_list_last_item = str(number_list[-1])
        print ("the sum of " + custom_formatter(number_list[:-1]) + " and " + number_list_last_item + " is " + str(sum))
    elif len(number_list) == 1:
        print ("the response is " + str(sum))
    else:
        print("empty list")
        
def custom_formatter(number_list: list[int]):
    formatted_response = ", ".join(list(map(str,number_list)))
    return formatted_response


def subtraction_of_two_numbers(number_1 : int, number_2: int):
    difference = number_1 - number_2
    print("the difference of " + str(number_1) + "and" + str(number_2) + "is" + str(difference))


def products_of_two_numbers(number_1 : int, number_2: int):
    product = number_1 * number_2
    print("the product of " + str(number_1) + "and" + str(number_2) + "is" + str(product))

def division_of_two_numbers(number_1 : int, number_2: int):
    quotient = number_1 / number_2
    if number_2 ==0:
        print("division by zero is not possible")
    else:
        print("the quotient of " + str(number_1) + "and" + str(number_2) + "is" + str(quotient))
 
      
print_sum_of_number_list([1, 5, 6, 7, 8, 9])       
print_sum_of_number_list([1, 5])       
print_sum_of_number_list([5])       
print_sum_of_number_list([])       
#sum_of_single_natural_numbers(6)
#division_of_two_numbers(10, 5)

#words =  ["this", "is", "a", "sentence"]
#numbers = [1, 2, 3, 4, 5]
#print("--".join(words))
#print("--".join(list(map(str,numbers))))
#print(words[2:])
#print(words[-1])










































