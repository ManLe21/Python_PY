import unittest
from student_manager_module import Student

class TestStudent(unittest.TestCase):

    def test_initialization(self):
        student = Student("Man Min", 20, [70.5, 82.0])
        self.assertEqual(student.full_name, "Man Min")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grades, [70.5, 82.0])
        self.assertEqual(student.average_grade, (70.5 + 82.0) / 2)
        self.assertEqual(student.result, "passed")
        self.assertEqual(student.level, "College")
        self.assertIsNone(student.email)
        self.assertEqual(student.offline_lessons_time, 0)

    def test_result_failed(self):
        student = Student("Sam Smith", 16, [55.0, 49.0])
        self.assertEqual(student.result, "failed")

    def test_result_passed(self):
        student = Student("Tom Hanks", 22, [88.0, 91.5])
        self.assertEqual(student.result, "passed")

    def test_level_primary(self):
        # Age 17 should now be "Primary"
        student = Student("Jack Lee", 17, [45.0, 51.0])
        self.assertEqual(student.level, "Primary")

    def test_level_college(self):
        student = Student("Eva Brown", 19, [78.0, 82.0])
        self.assertEqual(student.level, "College")

    def test_average_grade_calculation(self):
        student = Student("Tom Hanks", 22, [88.0, 91.5])
        expected_average = (88.0 + 91.5) / 2
        self.assertEqual(student.average_grade, expected_average)

if __name__ == '__main__':
    unittest.main()
