""""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""


import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Имя должно содержать только буквы и начинаться с заглавной буквы.")
        instance.__dict__[self.name] = value

class Student:
    _name = NameValidator()

    def __init__(self, name, subjects_file):
        self._name = None
        self._validated_name = name
        self.__subjects = self.load_subjects(subjects_file)
        self.__marks = {subject: [] for subject in self.__subjects}
        self.__test_results = {subject: [] for subject in self.__subjects}

    def load_subjects(self, file):
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            subjects = next(reader)
            return subjects

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_mark(self, subject, mark):
        if subject not in self.__subjects:
            raise ValueError("Предмет не допустим.")
        if mark < 2 or mark > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.__marks[subject].append(mark)

    def add_test_result(self, subject, test_result):
        if subject not in self.__subjects:
            raise ValueError("Предмет не допустим.")
        if test_result < 0 or test_result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.__test_results[subject].append(test_result)

    def get_average_mark(self, subject):
        pass

    def get_average_test_result(self, subject):
        pass

    def get_overall_average_mark(self):
        pass

if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")
    student.add_mark("Математика", 4)
    student.add_mark("Физика", 5)
    student.add_test_result("Математика", 80)
    student.add_test_result("Физика", 90)





