max_students = 5  # Can be  dynamic
students_summary = [] #Using list instead of a string
student_count = 0
while student_count < max_students:
    while True:
        full_name = input("Enter your full name (letters only, max 30 characters): ").strip()
        if len(full_name) == 0:
            print("Invalid name. Full Name cannot be empty.")
        elif not full_name.replace(" ", "").isalpha():
            print("Invalid name. Please use letters only (no numbers or symbols).")
        elif len(full_name) > 30:
            print("Invalid name. Please keep it under 30 characters.")
        else:
            break
    print("Student's full name:", full_name)
    while True:
        try:
            age = int(input("Enter your age : "))
            if 0 < age < 18:
                level = "Primary School"
                print(f"{full_name}, you are a {level} Student.")
                break
            elif 18 <= age <= 65:
                level = "College"
                print(f"{full_name}, you are a {level} Student.")
                break
            else:
                print("Age is out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            avg_grade_previous = float(input("Enter your average grade for the previous year: "))
            avg_grade_current = float(input("Enter your average grade for the current year: "))
            if avg_grade_previous < 0 or avg_grade_current < 0:
                print("Grades cannot be negative. Please enter valid numbers.")
                continue
            avg_years = (avg_grade_current + avg_grade_previous) / 2
            if avg_years <= 50:
                result = "failed"
            else:
                result = "passed"
            print(f"You {result}.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    student_info = {
        "Name": full_name,
        "Age": age,
        "Level": level,
        "Average Grade": avg_years,
        "Result": result
    }
    students_summary.append(student_info)
    student_count += 1
    # Asking if the user wants to add another student
    if student_count < max_students:
        cont = input("Do you want to enter another student? (type 'no' to stop): ").strip().lower()
        if cont == 'no':
            break
#showing all students' data
print(students_summary)