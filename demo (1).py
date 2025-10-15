from models import Teacher, Student, Course

t1 = Teacher(1, "Ardit Kola", "ardit.kola@shkolla.al")
t2 = Teacher(2, "Elona Hoxha", "elona.hoxha@shkolla.al")

c1 = Course("PY101", "Python Bazë", 2, t1)
c2 = Course("DB102", "Baza të të Dhënave", 3, t1)
c3 = Course("WD103", "Web Design", 2, t2)

students = [
    Student(10, "Elira Deda", 12),
    Student(11, "Klodian Meta", 11),
    Student(12, "Ardi Lila", 12),
    Student(13, "Sara Gega", 10),
    Student(14, "Brikena Gjoni", 11),
    Student(15, "Noel Hoxha", 10),
]

c1.add_student(students[0])
c1.add_student(students[1])
try:
    c1.add_student(students[2])
except ValueError as e:
    print("Gabim:", e)

c2.add_student(students[2])
c2.add_student(students[3])
c3.add_student(students[4])
c3.add_student(students[5])

print("\nKURSET:")
for course in [c1, c2, c3]:
    emrat = ", ".join(s.full_name for s in course.students)
    print(f"- {course.code} \"{course.title}\" — {len(course.students)}/{course.capacity} studentë: {emrat}")

print("\nMËSUESIT:")
for teacher in [t1, t2]:
    kurselist = ", ".join(c.code for c in teacher.courses)
    print(f"- {teacher.full_name}: {kurselist}")

print("\nMAKS/MIN:")
all_courses = [c1, c2, c3]
max_course = max(all_courses, key=lambda c: len(c.students))
min_course = min(all_courses, key=lambda c: len(c.students))
print(f"- Max: {max_course.code} ({len(max_course.students)})")
print(f"- Min: {min_course.code} ({len(min_course.students)})")

try:
    Teacher(3, "Test", "gabimemail")
except ValueError as e:
    print("Gabim:", e)

try:
    Course("ERR101", "Gabim", 0, t1)
except ValueError as e:
    print("Gabim:", e)

try:
    c2.add_student(students[2])
except ValueError as e:
    print("Gabim:", e)
