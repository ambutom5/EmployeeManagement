<<<<<<< HEAD
import mysql.connector
from datetime import datetime

from MySQL_PyCharm.EmployeeManagementCRUD.gui import department, joining_date

=======
import  mysql.connector
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3

class Connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
<<<<<<< HEAD
            host = "localhost",
            user = "root",
            password = "Anu@mbu5",
            database = "luminar"
            )
            return self.connection
        except Exception as e:
            print(e)

class EmployeeManager(Connect):
    def post(self,**kwargs):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employeee (name,place,department,salary,joining_date) values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Employee Added")
=======
                host="localhost",
                user="root",
                password="Anu@mbu5",
                database="luminar"
            )
            return self.connection
        except Exception as e:
            return None

class Student(Connect):
    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into studentt (id,name,age,place) values (%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Student Added!")
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
        except Exception as e:
            print(e)

    def get(self):
        try:
<<<<<<< HEAD
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employeee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            print(record)
=======
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for row in record:
                print(row)
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
        except Exception as e:
            print(e)

    def get_id(self,id = None):
        try:
<<<<<<< HEAD
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employeee where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self,id = None):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("No Employee Found!")
            else:
                print(record)
=======
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record

        except Exception as e:
            return None

    def retrieve(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                print(record)

>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
<<<<<<< HEAD
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Employee Not Found!")
            else:
                query = "delete from employeee where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee Deleted!")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Employee Not Found!")
=======
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                query = "delete from studentt where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Student Deleted!")
        except Exception as e:
            print(e)

    def put(self,id = None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
<<<<<<< HEAD
                query = f"update employeee set {placeholder} where id = %s"
=======
                query = f"update studentt set {placeholder} where id = %s"
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
<<<<<<< HEAD
                print("Employee Updated!")
=======
                print("Student Updated")
>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
        except Exception as e:
            print(e)


<<<<<<< HEAD
employee_instance = EmployeeManager()
# employee_instance.post(name = "Anu",place = "Trissur",department = "ECE",salary = 70000, joining_date = datetime.today())
# employee_instance.get()
# employee_instance.get_id(id = 3)
# employee_instance.retrieve(id = 3)
# employee_instance.delete(id =3)
# employee_instance.put(id = 2,name = "Annu",place = "Trichi",department = "EEE",salary = 20000)
=======

student_instance = Student()
# student_instance.post(id = 6,name = "Mannu",age = 30,place = "Tirur")
# student_instance.get()
# student_instance.get_id(id = 5)
# student_instance.retrieve(id = 3)
# student_instance.delete(id = 6)
student_instance.put(id = 5,name = "Mannu",age = 30,place = "Tirur")






>>>>>>> b46f36ab78dabf625d91016570f64227642e43b3
