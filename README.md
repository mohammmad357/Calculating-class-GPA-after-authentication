# Authenticated Class GPA Calculator

[![Tests](https://github.com/mohammmad357/Calculating-class-GPA-after-authentication/actions/workflows/tests.yml/badge.svg)](https://github.com/mohammmad357/Calculating-class-GPA-after-authentication/actions/workflows/tests.yml)

A dependency-free Python gradebook that authenticates a teacher, collects grades for one or more subjects, calculates class averages, and separates passing and failing students on a 0–20 scale.

## Security model

Credentials are read from environment variables and are never stored in the repository. This is an educational command-line authentication example—not a production identity system.

### macOS and Linux

```bash
export GPA_USERNAME="teacher"
export GPA_PASSWORD="choose-a-password"
python identification.py
```

### PowerShell

```powershell
$env:GPA_USERNAME = "teacher"
$env:GPA_PASSWORD = "choose-a-password"
python identification.py
```

The password prompt uses `getpass`, so the value is not echoed to the terminal.

## Features

- Supports any positive number of students and subjects.
- Validates duplicate names, empty names, numeric input, and grade boundaries.
- Calculates a separate average for each subject.
- Reports passed and failed students using 10 as the passing grade.
- Exposes reusable, typed functions for authentication and grade analysis.

## Tests

```bash
python -m unittest -v
```

GitHub Actions runs the suite on Python 3.10–3.13 for every push and pull request.

## License

Released under the [MIT License](LICENSE).
