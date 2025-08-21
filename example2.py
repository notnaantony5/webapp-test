class Student:
    students_count = 0

    def __init__(self, name) -> None:
        self.increase_count()
        self.name = name

    def get_name(self):
        return self.name
    
    @staticmethod
    def do():
        print("Вызвали но доступа никуда нет")

    @classmethod
    def get_count(cls):
        return cls.students_count
    
    @classmethod
    def increase_count(cls):
        cls.students_count += 1

student = Student("Sasha")
print(student.get_name())
student2 = Student("Sasha")
print(Student.get_count())