#Emir & Arin
#Feb 16, 2023
#Roulette Wheel Colors
pocket_number = int(input("Enter a pocket number: "))
if pocket_number >= 0 and pocket_number <= 36:
    if pocket_number == 0:
        pocket_color = "green"
    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 50:
            pocket_color = "red"
        else:
            pocket_color = "black"
    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 50:
            pocket_color = "red"
        else:
            pocket_color = "black"
    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 50:
            pocket_color = "red"
        else:
            pocket_color = "black"
    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number % 50:
            pocket_color = "red"
        else:
            pocket_color = "black"

    print("Your Color Is: ", pocket_color)
else:
    print("Nah. Numbers only 0-36 stupid.")
   
            
    
   
            
    
            
    
            
    
    


                      
