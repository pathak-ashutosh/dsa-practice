class Student:
    def __init__(self, name, dob):
        """
        Represents a Student.
        
        Required params:
        name (string): name of the student
        dob (string): date of birth of the student
        """
        self.name = name
        self.dob = dob
    
    def __repr__(self):
        return f"{self.name} {self.dob}"
    
    def get_dob(self, name):
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


def hash(name):
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

def collision(index, students):
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

def linear_probing(index, name, dob, students):
    """
    Applies linear probing (keep checking for the next available place for the student in the list until found)
    
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
    print("Cannot insert Student. List exhausted!")
    
def insert(Student, students):
    index = hash(Student.name)
    if collision(index, students):
        print("Performing Linear Probing:")
        linear_probing(index, Student.name, Student.dob, students)
    else:
        students[index] = Student
        print(f"No collisions, Student inserted at {index}")

def main():
    # list size is set so that not more than 70% of it is filled when all elements are placed in it to avoid overflow
    LIST_SIZE = 10
    students = [None] * LIST_SIZE
    
    # example data
    student_names = ['Ada', 'Mike', 'Leo', 'Stan', 'Rob', 'Rick']
    student_dobs = ['12/05/2008', '11/28/2001', '07/09/2004', '02/30/2002', '04/10/2008', '01/01/2000']
    
    for name, dob in zip(student_names, student_dobs):
        student = Student(name, dob)
        insert(student, students)
    
    print("Final Students list: ")
    print(*students)

if __name__ == "__main__":
    main()