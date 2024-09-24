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
