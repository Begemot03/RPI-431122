class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print("Name:", self.firstname, self.lastname)
        print("Age:", self.age)


class Student(Person):
    current_student_id = 1  # Статическое поле для отслеживания текущего studentID

    def __init__(self, firstname, lastname, age, recordBook):
        super().__init__(firstname, lastname, age)
        self.studentID = Student.current_student_id
        self.recordBook = recordBook
        Student.current_student_id += 1  # Увеличиваем studentID для следующего студента

    def display(self):
        super().display()
        print("Student ID:", self.studentID)
        print("Record Book:")
        for grade, count in self.recordBook.items():
            print(f"{grade}: {count}")


class Professor(Person):
    current_professor_id = 1

    def __init__(self, firstname, lastname, age, degree):
        super().__init__(firstname, lastname, age)
        self.professorID = Professor.current_professor_id
        self.degree = degree
        Professor.current_professor_id += 1

    def display(self):
        super().display()
        print("Professor ID:", self.professorID)
        print("Degree:", self.degree)


# Создание трех объектов класса Student
student1 = Student("Alice", "Smith", 20, {"A": 5, "B": 3, "C": 1})
student2 = Student("Bob", "Johnson", 22, {"A": 4, "B": 4, "C": 2})
student3 = Student("Charlie", "Brown", 21, {"A": 3, "B": 5, "C": 1})

# Вывод информации о студентах
print("Student 1:")
student1.display()
print("\nStudent 2:")
student2.display()
print("\nStudent 3:")
student3.display()

print("\n")
# Создание трех объектов класса Professor
professor1 = Professor("John", "Doe", 45, "PhD")
professor2 = Professor("Jane", "Smith", 50, "MD")
professor3 = Professor("David", "Brown", 55, "PhD")

# Вывод информации о профессорах
print("Professor 1:")
professor1.display()
print("\nProfessor 2:")
professor2.display()
print("\nProfessor 3:")
professor3.display()