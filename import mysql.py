import mysql.connector
class StudentManagementSystem:
    def __init__(self, host='localhost', user='root', password='Abcxyz@01', database='ruas_student_management_system'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

        # Create tables if they do not exist
        self.create_tables()

    def create_tables(self):
        # Define table creation queries
        create_student_table = '''
            CREATE TABLE IF NOT EXISTS Student (
                EnrollmentNumber INT PRIMARY KEY,
                Name VARCHAR(255),
                Address VARCHAR(255),
                ContactNumber VARCHAR(20),
                AdmissionDate DATE,
                BranchCode INT
            )
        '''

        create_branches_table = '''
            CREATE TABLE IF NOT EXISTS Branches (
                BranchCode INT PRIMARY KEY,
                BranchName VARCHAR(100),
                HODName VARCHAR(100)
            )
        '''

        create_fee_payments_table = '''
            CREATE TABLE IF NOT EXISTS FeePayments (
                PaymentID INT AUTO_INCREMENT PRIMARY KEY,
                EnrollmentNumber INT,
                PaymentDate DATE,
                Amount DECIMAL(10, 2),
                Mode VARCHAR(20),
                FOREIGN KEY (EnrollmentNumber) REFERENCES Student(EnrollmentNumber)
            )
        '''

        create_exam_results_table = '''
            CREATE TABLE IF NOT EXISTS ExamResults (
                ResultID INT AUTO_INCREMENT PRIMARY KEY,
                EnrollmentNumber INT,
                Semester INT,
                Subject VARCHAR(100),
                Marks INT,
                Grade CHAR(1),
                FOREIGN KEY (EnrollmentNumber) REFERENCES Student(EnrollmentNumber)
            )
        '''

        create_attendance_table = '''
            CREATE TABLE IF NOT EXISTS Attendance (
                AttendanceID INT AUTO_INCREMENT PRIMARY KEY,
                EnrollmentNumber INT,
                ClassDate DATE,
                Status VARCHAR(10),
                FOREIGN KEY (EnrollmentNumber) REFERENCES Student(EnrollmentNumber)
            )
        '''

        create_library_books_table = '''
            CREATE TABLE IF NOT EXISTS LibraryBooks (
                BookID INT AUTO_INCREMENT PRIMARY KEY,
                Title VARCHAR(255),
                Author VARCHAR(100),
                Available BOOLEAN
            )
        '''

        create_library_transactions_table = '''
            CREATE TABLE IF NOT EXISTS LibraryTransactions (
                TransactionID INT AUTO_INCREMENT PRIMARY KEY,
                EnrollmentNumber INT,
                BookID INT,
                TransactionDate DATE,
                DueDate DATE,
                Returned BOOLEAN,
                FOREIGN KEY (EnrollmentNumber) REFERENCES Student(EnrollmentNumber),
                FOREIGN KEY (BookID) REFERENCES LibraryBooks(BookID)
            )
        '''

        # Execute table creation queries
        self.cursor.execute(create_student_table)
        self.cursor.execute(create_branches_table)
        self.cursor.execute(create_fee_payments_table)
        self.cursor.execute(create_exam_results_table)
        self.cursor.execute(create_attendance_table)
        self.cursor.execute(create_library_books_table)
        self.cursor.execute(create_library_transactions_table)

        # Commit changes
        self.conn.commit()

    def add_student(self, enrollment_number, name, address, contact_number, admission_date, branch_code):
        try:
            self.cursor.execute('''
                INSERT INTO Student 
                (EnrollmentNumber, Name, Address, ContactNumber, AdmissionDate, BranchCode)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (enrollment_number, name, address, contact_number, admission_date, branch_code))
            self.conn.commit()
            print("Student added successfully!")
        except Exception as e:
            print(f"Error adding student: {e}")
    def delete_student(self, enrollment_number):
        try:
            self.cursor.execute('''
                DELETE FROM Student
                WHERE EnrollmentNumber = %s
            ''', (enrollment_number,))
            self.conn.commit()
            print("Student deleted successfully!")
        except Exception as e:
            print(f"Error deleting student: {e}")

    def view_students(self):
        self.cursor.execute('SELECT * FROM Student')
        students = self.cursor.fetchall()

        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    def add_branch(self, branch_code, branch_name, hod_name):
        try:
            self.cursor.execute('''
                INSERT INTO branches 
                (BranchCode, BranchName, HODName)
                VALUES (%s, %s, %s)
            ''', (branch_code, branch_name, hod_name))
            self.conn.commit()
            print("Branch added successfully!")
        except Exception as e:
            print(f"Error adding branch: {e}")
    def delete_branch(self, branch_code):
        try:
            self.cursor.execute('''
                DELETE FROM branches and Student
                WHERE BranchCode = %s
            ''', (branch_code,))
            self.conn.commit()
            print("Branch deleted successfully!")
        except Exception as e:
            print(f"Error deleting branch: {e}")
    def view_branches(self):
        self.cursor.execute('SELECT * FROM branches')
        branches = self.cursor.fetchall()

        if branches:
            for branch in branches:
                print(branch)
        else:
            print("No branches found.")

if __name__ == "__main__":
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Branch")
        print("5. View Branches")
        print("6.Delete Branch")
        print("7.Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            enrollment_number = int(input("Enter Enrollment Number: "))
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            contact_number = input("Enter Contact Number: ")
            admission_date = input("Enter Admission Date (YYYY-MM-DD): ")
            branch_code = input("Enter Branch Code: ")

            sms.add_student(enrollment_number, name, address, contact_number, admission_date, branch_code)

        elif choice == '2':
            sms.view_students()

        elif choice == '3':
            enrollment_number = input("Enter Enrollment Number to delete: ")
            sms.delete_student(enrollment_number)
            
        elif choice == '4':
            branch_code = input("Enter Branch Code: ")
            branch_name = input("Enter Branch Name: ")
            hod_name = input("Enter HOD Name: ")

            sms.add_branch(branch_code, branch_name, hod_name)
            break
        elif choice == '5':
            sms.view_branches()
        
        elif choice == '6':
            branch_code = input("Enter Branch Code to delete: ")
            sms.delete_branch(branch_code)
        elif choice == '7':
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please enter 1, 2,3,4,5,6 or 7")
