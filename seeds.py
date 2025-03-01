from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Subject, Teacher, Grade

# Ініціалізація Faker
fake = Faker()

# Створення підключення до бази даних
DATABASE_URL = 'postgresql://postgres:0967181951@localhost/my-db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Створення бази даних (якщо ще не створена)
Base.metadata.create_all(engine)

# Створення випадкових даних

# Створення груп
groups = []
for _ in range(3):  # 3 групи
    group_name = fake.word()
    group = Group(name=group_name)
    groups.append(group)

session.add_all(groups)
session.commit()

# Створення викладачів
teachers = []
for _ in range(3):  # 3 викладачі
    teacher_name = fake.name()
    teacher = Teacher(name=teacher_name)
    teachers.append(teacher)

session.add_all(teachers)
session.commit()

# Створення предметів
subjects = []
for _ in range(5):  # 5-8 предметів
    subject_name = fake.word()
    subject = Subject(name=subject_name, teacher_id=fake.random_element(teachers).id)
    subjects.append(subject)

session.add_all(subjects)
session.commit()

# Створення студентів
students = []
for _ in range(30):  # 30-50 студентів
    student_name = fake.name()
    student_group = fake.random_element(groups)
    student = Student(name=student_name, group_id=student_group.id)
    students.append(student)

session.add_all(students)
session.commit()

# Створення оцінок
grades = []
for student in students:
    # Генеруємо оцінки для кожного студента
    for subject in subjects:
        grade_value = fake.random_element([2, 3, 4, 5])  # Оцінки між 2 і 5
        grade = Grade(student_id=student.id, subject_id=subject.id, grade=grade_value)
        grades.append(grade)

session.add_all(grades)
session.commit()

print("База даних успішно заповнена випадковими даними.")
