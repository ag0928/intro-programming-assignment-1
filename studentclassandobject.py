class student:
    def __init__(self,stu_name,roll_no,p_marks=0.0,c_marks=0.0,m_marks=0.0,b_marks=0.0):
        self.stu_name=stu_name
        self.roll_no=roll_no
        self.p_marks=p_marks
        self.c_marks=c_marks
        self.m_marks=m_marks
        self.b_marks=b_marks
        self.total=0.0
        self.avg=0.0

    def calc(self):
        self.total=self.p_marks+self.c_marks+self.m_marks+self.b_marks
        self.avg=self.total/4
        print("-----------------------------------")


    def stu_details(self):
        self.stu_name=input("Enter Student Name :")
        self.roll_no=int(input("Enter Roll No. :"))
        self.p_marks=float(input("Enter Physics Marks :"))
        self.c_marks=float(input("Enter Chemistry Marks :"))
        self.m_marks=float(input("Enter Maths Marks :"))
        self.b_marks=float(input("Enter Biology Marks :"))

    def display_info(self):
        print("Student Name :",self.stu_name)
        print("Roll No :",self.roll_no)
        print("Total Marks: ",self.total)
        print("Average Marks: ",self.avg)


s=student("","")
s.stu_details()
s.calc()
s.display_info()