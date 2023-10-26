user_pocket_number = int(input("Enter a pocket number: "))

if user_pocket_number >= 0 and user_pocket_number <= 36:
    
    if user_pocket_number == 0:
        user_pocket_color = "green"
    
    elif user_pocket_number >= 1 and user_pocket_number <= 10:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "black"
        else:
            user_pocket_color = "red"

    elif user_pocket_number >= 11 and user_pocket_number <= 18:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "red"
        else:
            user_pocket_color = "black"
    
    elif user_pocket_number >= 19 and user_pocket_number <= 28:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "black"
        else:
            user_pocket_color = "red"

    elif user_pocket_number >= 29 and user_pocket_number <= 36:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "red"
        else:
            user_pocket_color = "black"

    print("User pocket color = ", user_pocket_color)
else:
    print("Error. Number must be between 0 and 36.\nRerun program and try again.")
