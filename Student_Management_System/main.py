from student import Student, HybridStudent


def main():
    students = []
    max_students = 5

    while len(students) < max_students:
        student_type = input("Enter student type (regular/hybrid): ").strip().lower()
        if student_type == "hybrid":
            student = HybridStudent()
        else:
            student = Student()


        while True:
            try:
                offline_time = float(input("Enter offline lessons time (hours): "))
                if offline_time < 0:
                    print("Please enter a positive number.")
                    continue
                student.add_offline_lessons_time(offline_time)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")


        if isinstance(student, HybridStudent):
            while True:
                try:
                    online_time = float(input("Enter online lessons time (hours): "))
                    if online_time < 0:
                        print("Please enter a positive number.")
                        continue
                    student.add_online_lessons_time(online_time)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        students.append(student)

        if len(students) < max_students:
            cont = input("Do you want to enter another student? (type 'no' to stop): ").strip().lower()
            if cont == 'no':
                break

    print("\n--- All Students Summary ---")
    for i, s in enumerate(students):
        s.display_summary(i)

if __name__ == "__main__":
    main()
