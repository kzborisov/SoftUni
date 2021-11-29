import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def test_student_initialization__when_no_courses__expected_empty_dict(self):
        name = "name"
        student = Student(name)
        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_student_initialization__when_courses(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        self.assertEqual(name, student.name)
        self.assertEqual(course, student.courses)

    def test_enroll__when_course_in_courses__expected_valid_message(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_course = "Python"
        new_notes = ["n2", "n3"]
        expected = "Course already added. Notes have been updated."
        actual = student.enroll(new_course, new_notes)
        all_notes = ["n1"] + new_notes
        self.assertEqual(expected, actual)
        self.assertEqual(all_notes, student.courses[new_course])
        self.assertTrue(new_course in student.courses)

    def test_enroll__when_course_not_in_courses_and_add_notes_is_y__expected_valid_message(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_course = "JavaScript"
        new_notes = ["n2", "n3"]
        expected = "Course and course notes have been added."
        actual = student.enroll(new_course, new_notes, "Y")
        self.assertEqual(expected, actual)
        self.assertTrue(new_course in student.courses)
        self.assertEqual(new_notes, student.courses[new_course])

    def test_enroll__when_course_not_in_courses_and_add_notes_is_empty_string__expected_valid_message(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_course = "JavaScript"
        new_notes = ["n2", "n3"]
        expected = "Course and course notes have been added."
        actual = student.enroll(new_course, new_notes, "")
        self.assertEqual(expected, actual)
        self.assertTrue(new_course in student.courses)
        self.assertEqual(new_notes, student.courses[new_course])

    def test_enroll_when_course_not_in_courses_and_not_add_notes__expect_valid_string(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_course = "JavaScript"
        new_notes = ["n2", "n3"]
        expected = "Course has been added."
        actual = student.enroll(new_course, new_notes, "N")
        self.assertEqual(expected, actual)
        self.assertTrue(new_course in student.courses)
        self.assertEqual([], student.courses[new_course])

    def test_add_notes__when_course_in_courses__expect_actual_result(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_notes = "n2"
        expected = "Notes have been updated"
        actual = student.add_notes("Python", new_notes)
        self.assertEqual(expected, actual)
        self.assertEqual(["n1", new_notes], student.courses["Python"])

    def test_add_notes__when_invalid_course__expect_exception(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        new_notes = "n2"
        expected = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as context:
            student.add_notes("JavaScript", new_notes)
        self.assertEqual(expected, str(context.exception))

    def test_leave_course__when_invalid_course__expect_exception(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        expected = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as context:
            student.leave_course("JavaScript")
        self.assertEqual(expected, str(context.exception))

    def test_leave_course__when_valid_course__expect_valid_message(self):
        name, course = "name", {"Python": ["n1"]}
        student = Student(name, course)
        expected = "Course has been removed"
        actual = student.leave_course("Python")
        self.assertEqual(expected, actual)
        self.assertEqual({}, student.courses)


if __name__ == "__main__":
    unittest.main()
