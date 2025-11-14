class Student:
    used_emails = set()

    def __init__(self):
        self._name = self._get_valid_name()
        self._age = self._get_valid_age()
        self._level = self._determine_level()
        self._grades = self._get_valid_grades()
        self._average_grade = self._calculate_average()
        self._result = self._determine_result()
        self._email = self._generate_unique_email()

        self._offline_lessons_time = 0  # private attribute for offline lessons (hours)

    # Encapsulated
    @property
    def name(self):
        return self._name

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


@property
    def age(self):
        return self._age
    x

    @property
    def level(self):
        return self._leveljj

    @property
    def grades(self):
        return self._grades

    @property
    def average_grade(self):
        return self._average_grade

    @property
    def result(self):
        return self._result

    @property
    def email(self):
        return self._email


    def add_offline_lessons_time(self, hours):
        if hours > 0:
            self._offline_lessons_time += hours
        else:
            print("Invalid offline lessons time. Must be positive.")

    def total_lessons_time(self):
        return self._offline_lessons_time


    def _get_valid_name(self):
        while True:
            full_name = input("Enter your full name (letters only, max 30 characters): ").strip().title()
            if len(full_name) == 0:
                print("Invalid name. Full Name cannot be empty.")
            elif not full_name.replace(" ", "").isalpha():
                print("Invalid name. Please use letters only (no numbers or symbols).")
            elif len(full_name) > 30:
                print("Invalid name. Please keep it under 30 characters.")
            else:
                return full_name

    def _get_valid_age(self):
        while True:
            try:
                age = int(input("Enter your age: "))
                if 0 < age <= 65:
                    return age
                else:
                    print("Age is out of range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def _determine_level(self):
        if self._age < 18:
            level = "Primary School"
        else:
            level = "College"
        print(f"{self._name}, you are a {level} student.")
        return level

    def _get_valid_grades(self):
        while True:
            try:
                previous = float(input("Enter your average grade for the previous year: "))
                current = float(input("Enter your average grade for the current year: "))
                if previous < 0 or current < 0:
                    print("Grades cannot be negative. Please enter valid numbers.")
                    continue
                return (previous, current)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def _calculate_average(self):
        return sum(self._grades) / 2

    def _determine_result(self):
        result = "passed" if self._average_grade > 50 else "failed"
        print(f"You {result}.")
        return result

    def _generate_unique_email(self):
        names = self._name.lower().split()
        first = names[0]
        last = names[-1] if len(names) > 1 else "student"
        base_email = f"{first}.{last}@myschool.armstqb"
        email = base_email
        counter = 1

        while email in Student.used_emails:
            email = f"{first}.{last}{counter}@myschool.armstqb"
            counter += 1

        Student.used_emails.add(email)
        return email

    def display_summary(self, index=None):
        key = f"Student #{index + 1}" if index is not None else "Student Summary"
        summary = {
            "Name": self._name,
            "Email": self._email,
            "Age": self._age,
            "Level": self._level,
            "Grades (Previous, Current)": self._grades,
            "Average Grade": round(self._average_grade, 2),
            "Result": self._result.capitalize(),
            "Offline Lessons Time (hours)": self._offline_lessons_time,
            "Total Lessons Time (hours)": self.total_lessons_time()
        }
        print({key: summary})


class HybridStudent(Student):
    def __init__(self):
        super().__init__()
        self._online_lessons_time = 0

    def add_online_lessons_time(self, hours):
        if hours > 0:
            self._online_lessons_time += hours
        else:
            print("Invalid online lessons time. Must be positive.")

    # Override total lessons time to include online + offline
    def total_lessons_time(self):
        return self._offline_lessons_time + self._online_lessons_time

    def display_summary(self, index=None):
        key = f"Hybrid Student #{index + 1}" if index is not None else "Hybrid Student Summary"
        summary = {
            "Name": self._name,
            "Email": self._email,
            "Age": self._age,
            "Level": self._level,
            "Grades (Previous, Current)": self._grades,
            "Average Grade": round(self._average_grade, 2),
            "Result": self._result.capitalize(),
            "Offline Lessons Time (hours)": self._offline_lessons_time,
            "Online Lessons Time (hours)": self._online_lessons_time,
            "Total Lessons Time (hours)": self.total_lessons_time()
        }
        print({key: summary})