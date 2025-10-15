class Teacher:
    def __init__(self, id, full_name, email):
        if id <= 0:
            raise ValueError("ID duhet të jetë > 0.")
        if "@" not in email:
            raise ValueError("Email jo i vlefshëm.")
        self.id = id
        self.full_name = full_name
        self.email = email
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Teacher[{self.id}] {self.full_name}"


class Student:
    def __init__(self, id, full_name, grade):
        if id <= 0:
            raise ValueError("ID duhet të jetë > 0.")
        if grade not in [10, 11, 12]:
            raise ValueError("Nota duhet të jetë 10–12.")
        self.id = id
        self.full_name = full_name
        self.grade = grade

    def __str__(self):
        return f"Student[{self.id}] {self.full_name} ({self.grade})"


class Course:
    def __init__(self, code, title, capacity, teacher):
        if not title.strip():
            raise ValueError("Titulli nuk mund të jetë bosh.")
        if capacity < 1:
            raise ValueError("Kapaciteti duhet të jetë ≥ 1.")
        self.code = code
        self.title = title
        self.capacity = capacity
        self.teacher = teacher
        self.students = []
        teacher.assign_course(self)

    def is_full(self):
        return len(self.students) >= self.capacity

    def add_student(self, student):
        if self.is_full():
            raise ValueError(f"Kursi {self.code} është plot.")
        if student in self.students:
            raise ValueError(f"{student.full_name} është regjistruar tashmë.")
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return f'Course[{self.code}] "{self.title}" ({len(self.students)}/{self.capacity}) — Teacher: {self.teacher.full_name}'
