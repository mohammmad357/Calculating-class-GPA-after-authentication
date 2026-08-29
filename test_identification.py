import unittest

from identification import authenticate, calculate_average, split_by_result, validate_grade


class GradebookTests(unittest.TestCase):
    def test_authentication(self) -> None:
        self.assertTrue(authenticate("teacher", "secret", "teacher", "secret"))
        self.assertFalse(authenticate("teacher", "wrong", "teacher", "secret"))
        self.assertFalse(authenticate("", "", "", ""))

    def test_grade_boundaries(self) -> None:
        self.assertEqual(validate_grade(0), 0)
        self.assertEqual(validate_grade(20), 20)

    def test_invalid_grades(self) -> None:
        for grade in (-0.1, 20.1, float("inf"), float("nan")):
            with self.subTest(grade=grade):
                with self.assertRaises(ValueError):
                    validate_grade(grade)

    def test_average(self) -> None:
        self.assertEqual(calculate_average({"Ali": 10, "Sara": 20}), 15)

    def test_empty_average(self) -> None:
        with self.assertRaises(ValueError):
            calculate_average({})

    def test_pass_fail_split(self) -> None:
        passed, failed = split_by_result({"Ali": 10, "Sara": 9.99, "Nima": 18})
        self.assertEqual(passed, {"Ali": 10.0, "Nima": 18.0})
        self.assertEqual(failed, {"Sara": 9.99})


if __name__ == "__main__":
    unittest.main()
