"""Authenticated class gradebook and GPA calculator.

Authentication is intentionally simple and configured through environment
variables. It is suitable for a command-line learning project, not as a
replacement for a production identity system.
"""

from __future__ import annotations

import hmac
import math
import os
from collections.abc import Mapping
from getpass import getpass


MIN_GRADE = 0.0
MAX_GRADE = 20.0
PASSING_GRADE = 10.0


def authenticate(
    username: str,
    password: str,
    expected_username: str,
    expected_password: str,
) -> bool:
    """Compare credentials without storing secrets in source code."""

    if not expected_username or not expected_password:
        return False
    return hmac.compare_digest(username, expected_username) and hmac.compare_digest(
        password, expected_password
    )


def validate_grade(value: float) -> float:
    """Return a valid finite grade on the 0–20 scale."""

    grade = float(value)
    if not math.isfinite(grade) or not MIN_GRADE <= grade <= MAX_GRADE:
        raise ValueError("Grade must be a finite number from 0 to 20.")
    return grade


def calculate_average(grades: Mapping[str, float]) -> float:
    """Calculate the average for a non-empty name-to-grade mapping."""

    if not grades:
        raise ValueError("At least one grade is required.")
    values = [validate_grade(grade) for grade in grades.values()]
    return sum(values) / len(values)


def split_by_result(grades: Mapping[str, float]) -> tuple[dict[str, float], dict[str, float]]:
    """Return passed and failed student mappings."""

    passed: dict[str, float] = {}
    failed: dict[str, float] = {}
    for name, value in grades.items():
        grade = validate_grade(value)
        (passed if grade >= PASSING_GRADE else failed)[name] = grade
    return passed, failed


def _read_positive_integer(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print("Please enter a positive whole number.")


def _read_grade(student: str, subject: str) -> float:
    while True:
        try:
            return validate_grade(float(input(f"{student} — {subject} grade: ").strip()))
        except ValueError as error:
            print(f"Error: {error}")


def _read_subjects() -> list[str]:
    while True:
        raw = input("Subjects, separated by commas (for example: Math, Physics): ")
        subjects = list(dict.fromkeys(part.strip() for part in raw.split(",") if part.strip()))
        if subjects:
            return subjects
        print("Please enter at least one subject.")


def collect_gradebook(student_count: int, subjects: list[str]) -> dict[str, dict[str, float]]:
    """Collect grades grouped by subject."""

    gradebook: dict[str, dict[str, float]] = {}
    for subject in subjects:
        grades: dict[str, float] = {}
        print(f"\n{subject}")
        for index in range(1, student_count + 1):
            while True:
                name = input(f"Student {index} name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                elif name in grades:
                    print("That student has already been entered for this subject.")
                else:
                    break
            grades[name] = _read_grade(name, subject)
        gradebook[subject] = grades
    return gradebook


def print_report(gradebook: Mapping[str, Mapping[str, float]]) -> None:
    for subject, grades in gradebook.items():
        passed, failed = split_by_result(grades)
        print(f"\n{subject} average: {calculate_average(grades):.2f}")
        print(f"Passed ({len(passed)}): {', '.join(passed) or 'none'}")
        print(f"Failed ({len(failed)}): {', '.join(failed) or 'none'}")


def main() -> int:
    expected_username = os.getenv("GPA_USERNAME", "")
    expected_password = os.getenv("GPA_PASSWORD", "")
    if not expected_username or not expected_password:
        print("Set GPA_USERNAME and GPA_PASSWORD before running this program.")
        return 2

    username = input("Username: ").strip()
    password = getpass("Password: ")
    if not authenticate(username, password, expected_username, expected_password):
        print("Access denied.")
        return 1

    print("Access granted.")
    student_count = _read_positive_integer("Number of students per subject: ")
    subjects = _read_subjects()
    print_report(collect_gradebook(student_count, subjects))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
