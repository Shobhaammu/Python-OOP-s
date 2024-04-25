class Student:
    def __init__(self,name,roll_number,password):
        self.name=name #public attribute
        self.roll_number=roll_number #protected attribute
        self.password=password #private attribute
        
    def display_details(self):
        print('Name:',self.name)
        print('Roll number:',self.roll_number)
        print('Password',self.password)
    def get_password(self):
        return self.password
    def set_password(self,new_password):
        self.password=new_password
        
student=Student(name='Alice',roll_number='A001',password ='secure_pass')
print('Name(pulic):',student.name)
print('Roll number (protected):',student.roll_number)
print('Password (private):',student.get_password())
student.set_password("new_password")
student.display_details()

