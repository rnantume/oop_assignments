class University:
    def __init__(self):
        self.students = ["John Red", "Paul Walter"]
        self.courses = ["MSCS","MSDS", "MIT"]
        self.lecturers = ["L001","L003","L007"]

    def list_students(self):
        return self.students

    def list_courses(self):
        return self.courses

    def list_lecturers(self):
        return self.lecturers
    
if __name__ == "__main__":
    university = University()
    
    print("Students:", university.list_students())
    print("Courses:", university.list_courses())
    print("Lecturers:", university.list_lecturers())