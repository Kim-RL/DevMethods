class Student:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        age=None,
        class_number=None,
        grades=None,
    ):
        # If no parameters provided at all, create default student
        if (
            first_name is None
            and last_name is None
            and age is None
            and class_number is None
            and grades is None
        ):
            self.first_name = "Vasya"
            self.last_name = "Pupkin"
            self.age = 16
            self.class_number = 11
            self.grades = [5, 5, 5]
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.class_number = class_number
            self.grades = list(grades) if grades is not None else []

    def show(self):
        print(
            f"{self.first_name} {self.last_name} {self.age} {self.class_number} {len(self.grades)}"
        )
        if self.grades:
            print(" ".join(str(g) for g in self.grades))
        else:
            print("")


def _read_non_empty_line():
    while True:
        try:
            line = input()
        except EOFError:
            return ""
        if line is None:
            return ""
        line = line.strip()
        if line != "":
            return line


def read_student():
    # First line: first_name last_name age class_number count
    first_line = _read_non_empty_line()
    if not first_line:
        # Fallback to default student if input prematurely ends
        return Student()
    parts = first_line.split()
    first_name = parts[0]
    last_name = parts[1]
    age = int(parts[2])
    class_number = int(parts[3])
    count = int(parts[4])

    grades_line = _read_non_empty_line()
    grades = [int(x) for x in grades_line.split()] if grades_line else []

    # If the provided count doesn't match, trust the actual grades read
    if len(grades) != count:
        # Optionally, truncate or ignore; here we keep what we read
        pass

    return Student(first_name, last_name, age, class_number, grades)


def print_all_students(students_journal):
    for student in students_journal:
        student.show()


if __name__ == "__main__":
    students = [read_student() for _ in range(5)]
    print_all_students(students)