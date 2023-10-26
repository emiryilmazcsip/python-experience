hw_avg = int(input("Whats your homework average?"))
lab_avg = int(input("Whats your lab average?"))
revel_avg = int(input("Whats your revel average?"))
mt_grade = int(input("Whats your mid term grade?"))
final_grade = int(input("Whats your final grade?"))
course_grade = hw_avg * 0.10 + lab_avg * 0.20 + revel_avg * 0.20 + mt_grade * 25 + final_grade * 0.25
print(course_grade)
