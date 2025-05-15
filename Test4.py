class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def average_grade(self):
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        return round(total / count, 1) if count > 0 else 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() != other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.average_grade()}"

    def average_grade(self):
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        return round(total / count, 1) if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() != other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def calculate_avg_hw_grade(students, course_name):
    total = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return round(total / count, 1) if count > 0 else 0


def calculate_avg_lecture_grade(lecturers, course_name):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return round(total / count, 1) if count > 0 else 0


# Создаем 2 экземпляра каждого класса
# Студенты
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Alice', 'Smith', 'female')
student2.courses_in_progress += ['Python', 'Django']
student2.finished_courses += ['Основы ООП']

# Лекторы
lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.courses_attached += ['Python', 'Django']

# Проверяющие
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached += ['Python', 'Django']

# Оцениваем домашние задания
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student1, 'Git', 7)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 9)

reviewer2.rate_hw(student2, 'Django', 10)
reviewer2.rate_hw(student2, 'Django', 9)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Git', 10)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Django', 9)

# Выводим информацию о всех созданных экземплярах
print("Информация о студентах:")
print(student1)
print()
print(student2)
print("\nИнформация о лекторах:")
print(lecturer1)
print()
print(lecturer2)
print("\nИнформация о проверяющих:")
print(reviewer1)
print()
print(reviewer2)

# Сравниваем студентов и лекторов
print("\nСравнение студентов:")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 <= student2: {student1 <= student2}")

print("\nСравнение лекторов:")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 >= lecturer2: {lecturer1 >= lecturer2}")

# Вызываем функции для подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

course = 'Python'
avg_hw = calculate_avg_hw_grade(students_list, course)
avg_lecture = calculate_avg_lecture_grade(lecturers_list, course)

print(f"\nСредняя оценка за домашние задания по курсу {course}: {avg_hw}")
print(f"Средняя оценка за лекции по курсу {course}: {avg_lecture}")