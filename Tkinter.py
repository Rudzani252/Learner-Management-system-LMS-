from tkinter import *
from tkinter import messagebox

from Classes import Course, Registration, Learner
from Assessments import Assessment
from SupportTicket import SupportTicket
from Singleton import AppConfig
config = AppConfig()



class LMS(Tk):
    def __init__(self):
        self.registration = Registration(registration_id="",learner="",course="",registration_date="",status="")
        self.course = Course(course_id="",course_name="",course_description="",duration="",price="",course_material="")
        self.learner = Learner(learner_id="",first_name="",last_name="",email="",phone_number="",password="",confPass="")
        self.assessment = Assessment(learner_id="",course_id="",assessment_name="",score="",result="")
        self.support_ticket = SupportTicket(learner_id="", learner_email="", ticket_type="", description="", status="")

        super().__init__()
        self.title("LMS")
        self.geometry("1400x600")

        self.login_frame = Frame(self)
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.register_frame = Frame(self)
        self.register_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.dashboard_frame = Frame(self)
        self.dashboard_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.courses_frame = Frame(self)
        self.courses_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.registration_frame = Frame(self)
        self.registration_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.assessment_frame = Frame(self)
        self.assessment_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.supportTicket_frame = Frame(self)
        self.supportTicket_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.viewCourse_frame = Frame(self)
        self.viewCourse_frame.place(x=0,y=0,relwidth=1,relheight=1)

        self.create_login()
        self.create_register()
        self.create_dashboard()
        self.create_courses()
        self.create_registration()
        self.create_assessments()
        self.create_supportTicket()
        

        self.show_frame(self.login_frame)
    def show_frame(self, frame):
        frame.tkraise()
        

    def login(self):
        

        email = self.email1.get()
        password = self.password1.get() 

        if not email or not password:
            messagebox.showerror(
            "Login",
            "Please enter username and password")
            return False
        else:
            result = self.learner.login(email, password)
            

            
            print(result)
            
            
            
            
            
           
            

            messagebox.showinfo("Success",
                                    "Welcome")
            self.show_frame(self.dashboard_frame)

                 

    def register_user(self):
        first_name = self.entryfirst_name.get()
        last_name = self.entrylastname.get()
        email = self.entryemail.get()
        password = self.entrypassword.get()
        confPass = self.entryconfPass.get()
        phone_num = self.entryphone_num.get()

        if not first_name or not last_name or not email or not password or not phone_num:
            messagebox.showerror("Error",
                                 "Fill in the form")
        elif password != confPass:
            messagebox.showerror("Error",
                                 "Passwaords dont match ")
        else:
             result = self.learner.register(first_name,last_name,email,password,confPass,phone_num )
             print(result)



    def create_login(self):


        self.email1 = Entry(self.login_frame)
        self.email1.place(x=400, y=150, relwidth=0.3, relheight=0.05)
        self.password1 = Entry(self.login_frame)
        self.password1.place(x=400, y=200, relwidth=0.3, relheight=0.05)

        Label(self.login_frame, text="Login",font="Arial90").place(x=570, y=50)
        Label(self.login_frame, text="Email").place(x=250, y=150)
        Label(self.login_frame, text="Password").place(x=250, y=200)

        Button(self.login_frame,text = "Register", command=lambda: self.show_frame(self.register_frame)).place(x =459, y = 300,relwidth=0.06, relheight=0.05)
        Button(self.login_frame, text="Login", command = self.login ).place(x=620, y=300,relwidth=0.06, relheight=0.05)
        
       


    def create_register(self):
        Label(self.register_frame, text="Register", font="Arial,90").place(x=570, y=50)
        Label(self.register_frame,text="First Name").place(x=250, y=150)
        Label(self.register_frame, text="Last name").place(x=250, y=200)
        Label(self.register_frame, text="Email").place(x=250, y=250)
        Label(self.register_frame, text="Password").place(x=250, y=300)
        Label(self.register_frame, text="Confirm Password").place(x=250, y=350)
        Label(self.register_frame, text="Phone Number").place(x=250, y=400)


        self.entryfirst_name = Entry(self.register_frame)
        self.entryfirst_name.place(x=400, y=150, relwidth=0.3, relheight=0.05)

        self.entrylastname= Entry(self.register_frame)
        self.entrylastname.place(x=400, y=200, relwidth=0.3, relheight=0.05)

        self.entryemail= Entry(self.register_frame)
        self.entryemail.place(x=400, y=250, relwidth=0.3, relheight=0.05)

        self.entrypassword = Entry(self.register_frame)
        self.entrypassword.place(x=400, y=300, relwidth=0.3, relheight=0.05)

        self.entryconfPass = Entry(self.register_frame)
        self.entryconfPass.place(x=400, y=350, relwidth=0.3, relheight=0.05)

        self.entryphone_num = Entry(self.register_frame)
        self.entryphone_num.place(x=400, y=400, relwidth=0.3, relheight=0.05)



        Button(self.register_frame, text="Register", command= self.register_user).place(x=620, y=450, relwidth=0.06, relheight=0.05)
        Button(self.register_frame, text="Back",command=lambda: self.show_frame(self.login_frame) ).place(x=459, y=450, relwidth=0.06, relheight=0.05)
        



    def create_dashboard(self):
        dashboard_title = Label(self.dashboard_frame,text="Dashboard",font=("Arial", 30, "bold"))
        dashboard_title.pack(pady =30)
        self.course_button = Button(self.dashboard_frame, text="Courses", command=lambda: self.show_frame(self.courses_frame)).place(x=620, y=300, relwidth=0.06, relheight=0.05)
        self.registration_button = Button(self.dashboard_frame, text="Registration",command=lambda: self.show_frame(self.registration_frame) ).place(x=520, y=300, relwidth=0.06, relheight=0.05)
        self.assessment_button = Button(self.dashboard_frame, text="Assessments", command=lambda: self.show_frame(self.assessment_frame)).place(x=720, y=300, relwidth=0.06, relheight=0.05)
        self.supportTicket_button = Button(self.dashboard_frame, text="Support Ticket ",command=lambda: self.show_frame(self.supportTicket_frame) ).place(x=820, y=300, relwidth=0.06, relheight=0.05)
        Button(self.dashboard_frame, text="Log Out",command=lambda: self.show_frame(self.login_frame) ).place(x=10, y=10, relwidth=0.06, relheight=0.05)


    def create_courses(self):
        Label(self.courses_frame,text="My Courses",font=("Arial", 30, "bold")).pack(pady=30)
        courses = self.course.display_courses()

        for course in courses:
            course_card = Frame(self.courses_frame,bd=2,relief="solid",padx=20,pady=15)
            course_card.pack(padx=100,pady=10,fill="x")
            Label(course_card,text=course["course_name"],font=("Arial", 18, "bold")).pack(anchor="w")
            Button(course_card,text="View Course",command=lambda c=course: self.create_viewCourse(c)).pack(anchor="e")
            Button(self.courses_frame,text="Back ",command=lambda: self.show_frame(self.dashboard_frame)).place(x =10, y=10,relwidth=0.06, relheight=0.05)



    def create_viewCourse(self, course):
        course_name = course["course_name"]
        course_data = self.course.display_course_material(course_name)

        if course_data is None:
            return

        for widget in self.viewCourse_frame.winfo_children():
         widget.destroy()

        Label(self.viewCourse_frame,text=course_data["course_name"],font=("Arial", 30, "bold")).pack(pady=30)
        Label(self.viewCourse_frame,text=course_data["course_description"],font=("Arial", 14),wraplength=700).pack(pady=20)
        Label(self.viewCourse_frame,text=course_data["duration"],font=("Arial", 14),wraplength=700).pack(pady=20)
        Label(self.viewCourse_frame,text=course_data["course_material"],font=("Arial", 14),wraplength=700).pack(pady=20)

        Button(self.viewCourse_frame,text="Back to Courses",command=lambda: self.show_frame(self.courses_frame)).pack(pady=20)
        Button(self.viewCourse_frame,text="Back ",command=lambda: self.show_frame(self.courses_frame)).place(x =10, y=10,relwidth=0.06, relheight=0.05)
        self.show_frame(self.viewCourse_frame)



    def create_registration(self):
        self.registration_courses = self.course.display_courses()
        self.course_listbox = Listbox(self.registration_frame,width=50,height=10)
        self.course_listbox.pack(pady=20)

        for course in self.registration_courses:
            self.course_listbox.insert(END,course["course_name"])

        Button(self.registration_frame,text="Register",command=self.register_selected_course).place(x=550, y=250, relwidth=0.22, relheight=0.05)
        Button(self.registration_frame,text="Back ",command=lambda: self.show_frame(self.dashboard_frame)).place(x =10, y=10,relwidth=0.06, relheight=0.05)

        Label(self.registration_frame,text="Email").place(x=500, y=200)
        self.entryEmail= Entry(self.registration_frame)
        self.entryEmail.place(x=550, y=200,relwidth=0.22, relheight=0.05)



    def register_selected_course(self):

        selected = self.course_listbox.curselection()
        index = selected[0]
        selected_course = self.registration_courses[index]
        course_id = selected_course["course_id"]
        learner_email = self.entryEmail.get()
        learner_id = self.learner.learner_id
        
        
        

        if not selected or not learner_email : 
            messagebox.showwarning("Please select a course or enter email")
            return 
        else: 
            

            result = self.registration.add_registration(learner_id, learner_email, course_id)
            print(result)

        

        print("Learner ID", learner_id)
        print("Email:", learner_email)
        print("Course ID:", course_id)

    def create_assessments(self):
        Label(self.assessment_frame,text="My Assessments",font=("Arial", 30, "bold")).pack(pady=30)
        Label(self.assessment_frame,text="Learner ID").place(x=450, y=120)
        self.entryLearnerID= Entry(self.assessment_frame,width=30)
        self.entryLearnerID.pack(pady=5)
        self.marks_text = Text(self.assessment_frame,width=65,height=15)
        self.marks_text.pack(pady=20)
        Button(self.assessment_frame,text="View My Marks",command=self.display_marks).pack(pady=10)
        Button(self.assessment_frame,text="Back ",command=lambda: self.show_frame(self.dashboard_frame)).place(x =10, y=10,relwidth=0.06, relheight=0.05)

    def display_marks(self):
        learner_id = self.entryLearnerID.get()
        if not learner_id:
            messagebox.showwarning(
                "Missing Information",
                "Please enter your learner ID")
            return
        else:
            marks = self.assessment.get_marks(learner_id)

        if isinstance(marks, list):

            for mark in marks:

                self.marks_text.insert(END,f"Assessment: {mark['assessment_name']}\n")

                self.marks_text.insert( END, f"Score: {mark['assessment_score']}\n")

                self.marks_text.insert( END,f"Result: {mark['assessment_result']}\n")

                self.marks_text.insert(END,f"Course ID: {mark['course_id']}\n")

                self.marks_text.insert(END,"-" * 50 + "\n")

        else:

            self.marks_text.insert(END,marks.get(
                    "message",
                    "No marks found"))

    def create_supportTicket(self):
        Label(self.supportTicket_frame,text="Create Support Ticket",font=("Arial", 30, "bold")).pack(pady=20)
        Label(self.supportTicket_frame,text="Learner Email:",font=("Arial", 12)).pack(pady=5)

        self.entryTicketEmail = Entry(self.supportTicket_frame,width=30)
        self.entryTicketEmail.pack(pady=5)

        Label(self.supportTicket_frame,text="Select Ticket Type:",font=("Arial", 12)).pack(pady=5)
        self.ticket_type_list = Listbox(self.supportTicket_frame,width=30,height=3,font=("Arial", 12),exportselection=False)
        self.ticket_type_list.insert(END, "Technical")
        self.ticket_type_list.insert(END, "Registration")
        self.ticket_type_list.insert(END, "Course")
        self.ticket_type_list.pack(pady=5)

        Label(self.supportTicket_frame,text="Description:",font=("Arial", 12)).pack(pady=5)
        self.ticket_description = Entry(self.supportTicket_frame, font=("Arial", 11))
        self.ticket_description.pack(pady=10)

        Button(self.supportTicket_frame,text="Submit Ticket",command=self.submit_ticket).pack(pady=10)
        Button(self.supportTicket_frame,text="Back ",command=lambda: self.show_frame(self.dashboard_frame)).place(x =10, y=10,relwidth=0.06, relheight=0.05)

    def submit_ticket(self):
        selected_ticket = self.ticket_type_list.curselection()
        learner_email = self.entryTicketEmail.get()
        learner_id = self.learner.learner_id
        description = self.ticket_description.get()


        if not learner_email:
            messagebox.showwarning(
            "Missing Information",
            "Please enter your email")
            return
        elif not description:
            messagebox.showwarning(
            "Missing Information",
            "Please enter a ticket description")
            return
        elif not selected_ticket:
            messagebox.showwarning(
            "Missing Information",
            "Please select a ticket type")
            return
        else: 
            ticket_type = self.ticket_type_list.get(selected_ticket[0])
            result = self.support_ticket.create_ticket(learner_id, learner_email, ticket_type, description)
            messagebox.showinfo(
                        "Success",
                        "Ticket opened")
            print(result)
            







       



        



       




if __name__ == '__main__':
    app = LMS()
    app.mainloop()
