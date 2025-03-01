from sqlalchemy.orm import aliased
from sqlalchemy import func
from models import Student, Grade, Group, Teacher, Subject
from connect import session  # Імпортуємо session з файлу connect


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    results = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return results


# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_id):
    results = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(
        func.avg(Grade.grade).desc()).first()
    return results


# 3. Знайти середній бал у групах з певного предмета
def select_3(subject_id):
    results = session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Group.students).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return results


# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    results = session.query(
        func.avg(Grade.grade).label('average_grade')
    ).all()
    return results


# 5. Знайти які курси читає певний викладач
def select_5(teacher_id):
    results = session.query(
        Subject.name
    ).join(Teacher).filter(Subject.teacher_id == teacher_id).all()
    return results


# 6. Знайти список студентів у певній групі
def select_6(group_id):
    results = session.query(
        Student.name
    ).join(Group).filter(Group.id == group_id).all()
    return results


# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_id, subject_id):
    results = session.query(
        Student.name,
        Grade.grade
    ).join(Group).join(Grade).filter(Group.id == group_id, Grade.subject_id == subject_id).all()
    return results


# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id):
    grade_alias = aliased(Grade)
    return session.query(func.avg(grade_alias.grade).label("average_grade")).join(Subject,
                                                                                  grade_alias.subject_id == Subject.id).filter(
        Subject.teacher_id == teacher_id).all()


# 9. Знайти список курсів, які відвідує певний студент
def select_9(student_id):
    return session.query(Subject.name.label("subjects_name")).join(Grade, Grade.subject_id == Subject.id).filter(
        Grade.student_id == student_id).all()


# 10. Список курсів, які певному студенту читає певний викладач
def select_10(student_id, teacher_id):
    return session.query(Subject.name.label("subjects_name")).join(Grade, Grade.subject_id == Subject.id).filter(
        Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()

#11. Середній бал, який певний викладач ставить певному студенту:
def select_11(student_id, teacher_id):
    return session.query(func.avg(Grade.value).label("average_grade")) \
        .join(Subject).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id) \
        .all()

