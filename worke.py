class Classroom:

    def __init__(self, room_name):
        self.room_name = room_name
        self._teacher = "Not assigned yet"
        self.__students = []

    # Set teacher
    def set_teacher(self, teacher_name):
        self._teacher = teacher_name

    # Get teacher
    def get_teacher(self):
        return self._teacher

    # Add student
    def addStudent(self, name, age, course):
        student = {
            "name": name,
            "age": age,
            "course": course
        }

        self.__students.append(student)
        print(name, "has been added successfully!")

    # Display students
    def displayStudents(self):
        if len(self.__students) == 0:
            print("No students found.")
        else:
            print("\nStudents in", self.room_name)
            print("Teacher:", self._teacher)
            print("Total Students:", len(self.__students))
            print("--------------------")

            for student in self.__students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("--------------------")

    # Search student
    def searchStudent(self, name):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                return

        print("No Student Found.")

    # Count students
    def studentCount(self):
        print("Total Students:", len(self.__students))

    # Update course
    def updateCourse(self, name, new_course):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            if student["name"].lower() == name.lower():
                old_course = student["course"]
                student["course"] = new_course

                print("\nCourse updated successfully!")
                print("Student:", student["name"])
                print("Old Course:", old_course)
                print("New Course:", new_course)
                return

        print("No Student Found.")

    # Delete student
    def deleteStudent(self, name):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            if student["name"].lower() == name.lower():
                self.__students.remove(student)

                print("\n", name, "has been deleted successfully!")
                print("Total Students:", len(self.__students))
                return

        print("No Student Found.")


# -------------------
# Testing
# -------------------

room1 = Classroom("Room A")

room1.set_teacher("Mr. Smith")
print("Teacher:", room1.get_teacher())

room1.displayStudents()

room1.addStudent("John", 20, "Python")
room1.addStudent("Alice", 22, "Java")
room1.addStudent("Mike", 21, "C++")

print("\nCurrent Students:")
room1.displayStudents()

room1.studentCount()

room1.searchStudent("John")
room1.searchStudent("David")

room1.updateCourse("John", "Data Science")

print("\nAfter Course Update:")
room1.displayStudents()

room1.deleteStudent("Alice")

print("\nAfter Deleting Alice:")
room1.displayStudents()

room1.studentCount()