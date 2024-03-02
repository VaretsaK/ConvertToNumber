def convert_to_number():

    try:
        user_input_1 = int(input("Enter first number: "))
        user_input_2 = int(input("Enter second number: "))
    except ValueError:
        return "You have to input only digits."
    else:
        return [user_input_1, user_input_2]
