def double_number(number):
    result_double_number = number * 2
    return result_double_number

def get_user_name():
    return input("whats your name? ")

def get_user_age():
    return input("How old are you? ")


def welcome_user():
    user_name = get_user_name()
    print("Hello " + str(user_name) + "!")
    user_age = get_user_age()
    print("you are " + str(user_age) + ". welcome")
    
    
#welcome_user("gaby", "5")
#print(double_number(4))





