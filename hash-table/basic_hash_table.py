class Student:
    def __init__(self, name: str, dob: str):
        """
        Represents a Student.
        
        Required params:
        name (string): name of the student
        dob (string): date of birth of the student
        """
        self.name = name
        self.dob = dob
    
    def __repr__(self):
        """
        String format of the object.
        """
        return f"({self.name} {self.dob})"
    
    def get_dob(self, name: str):
        """
        Gets the date of birth of the student, given their name.
        
        Params:
        self: the object of Student
        name (string): name of the student
        
        Returns:
        dob (string): date of birth of the student
        """
        if self.name == name:
            return self.dob
        return f"{name} does not exist"


def hash(name: str):
    """
    Hashing function that uses the name to calculate the index where it will be stored.
    
    Params:
    name (string): the name of the student
    
    Returns:
    index (int): the index where the name will be stored
    """
    # split the string into letters
    letters = [*name]
    ascii_sum = 0
    # get ascii value of each letter and add them together
    for letter in letters:
        ascii_sum += ord(letter)
    # calculate the index for placing the item
    index = ascii_sum % len(letters)
    print(f"Calculated index for {name}: {index}")
    return index

def collision(index: int, students: list):
    """
    Checks whether the index given by the hash function collides with another student.
    
    Params:
    index (int): index from the hash function
    students (list): the list of students
    
    Returns:
    bool: True if collision occurs, False otherwise
    """
    if students[index]:
        print("Collision detected!")
        return True
    return False

def linear_probing(index: int, name: str, dob: str, students: list):
    """
    Applies linear probing (keeps checking for the next available place in the list until found)
    
    Params:
    index (int): index returned by the hash function
    name (string): the name of the student to insert
    dob (string): date of birth of the student
    students (list): list of students so far
    
    Returns:
    students (list): list of students with the new student
    """
    for i in range(index + 1, len(students) - 1):
        print(f"Checking index {i}...")
        if not students[i]:
            students[i] = Student(name, dob)
            print(f"Student inserted at {i}")
            return students
    print("Cannot insert Student. List exhausted!")
    
def insert(Student: Student, students: list):
    """
    Inserts the given student to the list
    
    Params:
    student_name (string): name of the student to find
    students (list): the list of students
    
    Does not return.
    """
    index = hash(Student.name)
    if collision(index, students):
        print("Performing Linear Probing:")
        linear_probing(index, Student.name, Student.dob, students)
    else:
        students[index] = Student
        print(f"No collisions, Student inserted at {index}")

def initialize_list(students: list, student_names: list, student_dobs: list):
    """
    Initializes the entire list with the given students
    
    Params:
    students (list -> Student): list of Students
    student_names (list -> string): list of student names
    student_dobs (list -> string): list of students' dates of birth
    """
    # insert students into the list
    for name, dob in zip(student_names, student_dobs):
        student = Student(name, dob)
        insert(student, students)
        
    return students

def find_student(student_name: str, students: list):
    """
    Finds the student in the list by thier name.
    
    Params:
    student_name (string): name of the student to find
    students (list): the list of students
    
    Returns:
    student (Student): the Student object of the student_name, if found
    """
    index = hash(student_name)
    print(f"\nFinding {student_name}:")
    print(f"Calculated index: {index}")
    # perform linear probing
    for i in range(index, len(students) - 1):
        print(f"Checking index {i}...")
        if students[i]:
            if students[i].name == student_name:
                print(f"Student found at {i}: {students[i]}")
                return students
    print(f"Cannot find {student_name}. List exhausted!")


def main():
    # example data
    student_names = ['Ada', 'Mike', 'Leo', 'Stan', 'Rob', 'Rick']
    student_dobs = ['12/05/2008', '11/28/2001', '07/09/2004', '02/30/2002', '04/10/2008', '01/01/2000']
    
    # list size is set so that not more than 70% of it is filled when all elements are placed in it to avoid overflow
    LIST_SIZE = 10
    students = [None] * LIST_SIZE
    students = initialize_list(students, student_names, student_dobs)
    print("Final Students list: ", [*students])
    
    # find a student by their name
    find_student(student_names[3], students)

if __name__ == "__main__":
    main()