class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.finished_courses and course in lector.courses_attached:
            rating_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if course in lector.grades and grade in rating_scale:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        av_value = self.av_grades()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {round(av_value, 1)} \nКурсы в процессе изучения:{", ".join(self.courses_in_progress)} \nЗавершенные курсы:{", ".join(self.finished_courses)}'

    def av_grades(self):
        av_value = float(0)
        if self.grades:
            for value in self.grades.values():
                av_value += sum(value)
            av_value = av_value / len(self.grades)
        return av_value

    def __lt__(self, other):
        return self.av_grades() < other.av_grades()

    def __le__(self, other):
        return self.av_grades() <= other.av_grades()

    def __gt__(self, other):
        return self.av_grades() > other.av_grades()

    def __ge__(self, other):
        return self.av_grades() >= other.av_grades()

    def __eq__(self, other):
        return self.av_grades() == other.av_grades()

    def __ne__(self, other):
        return self.av_grades() != other.av_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.courses_attached = []
        self.grades = {}

    def av_grades(self):
        av_value = float(0)
        if self.grades:
            for value in self.grades.values():
                av_value += sum(value)
            av_value = av_value / len(self.grades)
        return av_value

    def __lt__(self, other):
        return self.av_grades() < other.av_grades()

    def __le__(self, other):
        return self.av_grades() <= other.av_grades()

    def __gt__(self, other):
        return self.av_grades() > other.av_grades()

    def __ge__(self, other):
        return self.av_grades() >= other.av_grades()

    def __eq__(self, other):
        return self.av_grades() == other.av_grades()

    def __ne__(self, other):
        return self.av_grades() != other.av_grades()

    def __str__(self):
        av_values = self.av_grades()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(av_values, 1)}'





class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    # студент 1
    student_1 = Student('Джессика', 'Альба', 'ж')
    student_1.finished_courses = ['Git']
    student_1.courses_in_progress = ['CSS', 'Java']
    print(student_1)

    # студент 2
    student_2 = Student('Бэтмен', 'Иванов', 'м')
    student_2.finished_courses = ['C#']
    student_2.courses_in_progress = ['SQL', 'Java']
    print(student_2)

    # лектор 1
    lecturer_1 = Lecturer('Альфред', 'Петров')
    lecturer_1.courses_attached = ['SQL']
    print(lecturer_1)

    # лектор 2
    lecturer_2 = Lecturer('Борис', 'Кац')
    lecturer_2.courses_attached = ['Java']
    print(lecturer_2)

    # ревьювер 1
    reviewer_1 = Reviewer('Джон', 'Сидоров')
    reviewer_1.courses_attached = ['Git']
    print(reviewer_1)

    # ревьювер 2
    reviewer_2 = Reviewer('Ким', 'Чен Ыр')
    reviewer_2.courses_attached = ['С++']
    print(reviewer_2)

    # проверка методов
    student_1.rate_lec(lecturer_1, 'Git', 10)  # несотв. лектора и курса
    student_1.rate_lec(lecturer_1, 'Python', 8)
    student_2.rate_lec(lecturer_1, 'Python', 10)
    student_2.rate_lec(lecturer_2, 'Git', 5)
    print('Оценки 1-го преподавателя', lecturer_1.grades)

    reviewer_1.rate_hw(student_1, 'Python', 7)
    reviewer_1.rate_hw(student_1, 'Git', 7)
    print(f'Оценки 1-го студента {student_1.grades}')

    reviewer_2.rate_hw(student_2, 'Git', 9)
    reviewer_1.rate_hw(student_2, 'Python', 6)
    print(f'Оценки 2-го студента {student_2.grades}')

    # сравнение студентов
    print(student_1.av_grades(), student_2.av_grades())
    print(student_1 > student_2)
    print(student_1 == student_2)
    print(student_1 < student_2)

    # сравнение лекторов
    print(lecturer_1.av_grades(), lecturer_2.av_grades())
    print(lecturer_1 > lecturer_2)
    print(lecturer_1 == lecturer_2)
    print(lecturer_1 < lecturer_2)

    # методы подсчета средней оценки

    def average_rating_hw(students: list, course: str):
        rating, count = 0, 0
        for student in students:
            if student.grades.get(course, None):
                rating += sum(student.grades[course])
                count += 1
        return rating / count if count != 0 else 'нет данных'

    def average_rating_lr(lectors: list, course: str):
        rating, count = 0, 0
        for lector in lectors:
            if lector.grades.get(course, None):
                rating += sum(lector.grades[course])
                count += 1
        return rating / count if count != 0 else 'нет данных'

    print(average_rating_hw([student_1, student_2], 'Python'))
    print(average_rating_hw([student_1, student_2], 'Git'))
    print(average_rating_hw([student_1, student_2], 'Java'))
    print()
    print(average_rating_lr([lecturer_1, lecturer_2], 'Python'))
    print(average_rating_lr([lecturer_1, lecturer_2], 'Git'))
    print(average_rating_lr([lecturer_1, lecturer_2], 'Java'))