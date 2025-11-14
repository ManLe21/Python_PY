import json

def read_students_from_txt(file_path):
    students = []
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            # Every student has 3 lines: name, age, grades
            for i in range(0, len(lines), 3):
                name = lines[i]
                age = int(lines[i+1])
                grades = tuple((float, lines[i+2].split(',')))
                students.append((name, age, grades))
    except Exception as e:
        print(f"Error reading from TXT: {e}")
    return students


def read_students_from_json(file_path):
    students = []
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for entry in data:
                name = entry.get("full_name")
                age = entry.get("age")
                grades = tuple(entry.get("grades"))
                students.append((name, age, grades))
    except Exception as e:
        print(f"Error reading from JSON: {e}")
    return students


from student import (
    get_valid_name,
    get_valid_age_and_level,
    get_grades_and_result,
    generate_email,
    read_students_from_txt,
    read_students_from_json
)

used_emails = set()
students_summary = []

# --- Select Input Type ---
input_type = input("Choose input type (manual / file / json): ").strip().lower()

if input_type == "manual":
    max_students = 5
    for _ in range(max_students):
        full_name = get_valid_name()
        age, _ = get_valid_age_and_level(full_name)
        grades, _, _ = get_grades_and_result()

        student = HybridStudent(full_name, age, grades)
        student.set_email(generate_email(full_name, used_emails))
        student.add_offline_lessons_time(float(input("Enter offline lesson time (hours): ")))
        student.add_online_lessons_time(float(input("Enter online lesson time (hours): ")))
        students_summary.append(student)

        cont = input("Add another? (type 'no' to stop): ").strip().lower()
        if cont == 'no':
            break

elif input_type == "file":
    file_path = input("Enter path to TXT file (e.g. students.txt): ").strip()
    students_data = read_students_from_txt(file_path)
    for name, age, grades in students_data:
        student = HybridStudent(name, age, grades)
        student.set_email(generate_email(name, used_emails))
        # For file-based, let's simulate lesson times
        student.add_offline_lessons_time(10)
        student.add_online_lessons_time(5)
        students_summary.append(student)
elif input_type == "json":
    file_path = input("Enter path to JSON file (e.g. students.json): ").strip()
    students_data = read_students_from_json(file_path)
    for name, age, grades in students_data:
        student = HybridStudent(name, age, grades)
        student.set_email(generate_email(name, used_emails))
        # Simulated lesson times
        student.add_offline_lessons_time(12)
        student.add_online_lessons_time(8)
        students_summary.append(student)

else:
    print("Invalid input type. Please restart and choose 'manual', 'file', or 'json'.")
