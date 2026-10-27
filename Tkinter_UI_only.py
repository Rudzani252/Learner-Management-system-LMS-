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
        self.geometry("1400x650")
        self.minsize(1180, 630)

        self.login_frame = Frame(self, bg="#f4f7fc")
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.register_frame = Frame(self, bg="#f4f7fc")
        self.register_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.dashboard_frame = Frame(self, bg="#f4f7fc")
        self.dashboard_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.courses_frame = Frame(self, bg="#f4f7fc")
        self.courses_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.registration_frame = Frame(self, bg="#f4f7fc")
        self.registration_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.assessment_frame = Frame(self, bg="#f4f7fc")
        self.assessment_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.supportTicket_frame = Frame(self, bg="#f4f7fc")
        self.supportTicket_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.viewCourse_frame = Frame(self, bg="#f4f7fc")
        self.viewCourse_frame.place(x=0,y=0,relwidth=1,relheight=1)
        self.profile_frame = Frame(self)
        self.profile_frame.place(x=0, y=0,relwidth=1, relheight=1)

        self.create_login()
        self.create_register()
        self.create_dashboard()
        self.create_courses()
        self.create_registration()
        self.create_assessments()
        self.create_supportTicket()
        self.create_profile()
        

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
        result = self.learner.login(email, password)
        print("Login result:",result)

        if isinstance(result, dict) and result.get("status") == "Success":
            messagebox.showinfo(
            "Success",
            "Welcome to the LMS!" )
            self.show_frame(self.dashboard_frame)
        else:
            messagebox.showerror(
            "Login Failed",
            "Invalid email or password"
        )
    
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
        Label(self.login_frame, text="LEARNSPACE  /  LMS", bg="#f4f7fc", fg="#4f46e5", font=("Segoe UI", 13, "bold")).place(relx=.5, y=54, anchor="center")
        Label(self.login_frame, text="Welcome back", bg="#f4f7fc", fg="#14213d", font=("Segoe UI", 33, "bold")).place(relx=.5, y=117, anchor="center")
        Label(self.login_frame, text="Sign in to continue learning", bg="#f4f7fc", fg="#64748b", font=("Segoe UI", 12)).place(relx=.5, y=162, anchor="center")
        Label(self.login_frame, text="Email address", bg="#f4f7fc", fg="#334155", font=("Segoe UI", 11, "bold")).place(relx=.5, x=-210, y=225)
        self.email1 = Entry(self.login_frame, font=("Segoe UI", 13), bg="white", fg="#0f172a", relief="solid", bd=1)
        self.email1.place(relx=.5, y=250, anchor="n", width=420, height=42)
        Label(self.login_frame, text="Password", bg="#f4f7fc", fg="#334155", font=("Segoe UI", 11, "bold")).place(relx=.5, x=-210, y=305)
        self.password1 = Entry(self.login_frame, font=("Segoe UI", 13), bg="white", fg="#0f172a", relief="solid", bd=1, show="*")
        self.password1.place(relx=.5, y=330, anchor="n", width=420, height=42)
        Button(self.login_frame, text="Log in", command=self.login, font=("Segoe UI", 12, "bold"), bg="#4f46e5", fg="white", activebackground="#4338ca", activeforeground="white", relief="flat", cursor="hand2").place(relx=.5, y=401, anchor="n", width=420, height=45)
        Button(self.login_frame, text="Create an account", command=lambda: self.show_frame(self.register_frame), font=("Segoe UI", 11), bg="#f4f7fc", fg="#4f46e5", relief="flat", cursor="hand2").place(relx=.5, y=462, anchor="n", width=230, height=35)

    def create_register(self):
        Label(self.register_frame, text="Create your account", font=("Segoe UI", 29, "bold"), bg="#f4f7fc", fg="#14213d").place(relx=.5, y=35, anchor="n")
        Label(self.register_frame, text="Join LearnSpace and start learning", font=("Segoe UI", 11), bg="#f4f7fc", fg="#64748b").place(relx=.5, y=87, anchor="n")
        fields = [
            ("First name", "entryfirst_name"), ("Last name", "entrylastname"),
            ("Email address", "entryemail"), ("Password", "entrypassword"),
            ("Confirm password", "entryconfPass"), ("Phone number", "entryphone_num")
        ]
        for i, (caption, attr) in enumerate(fields):
            col, row = i % 2, i // 2
            x = 370 + col * 350
            y = 142 + row * 107
            Label(self.register_frame, text=caption, bg="#f4f7fc", fg="#334155", font=("Segoe UI", 10, "bold")).place(x=x, y=y)
            field = Entry(self.register_frame, font=("Segoe UI", 12), bg="white", fg="#0f172a", relief="solid", bd=1, show="*" if attr in ("entrypassword", "entryconfPass") else "")
            field.place(x=x, y=y + 27, width=305, height=39)
            setattr(self, attr, field)
        Button(self.register_frame, text="Create account", command=self.register_user, font=("Segoe UI", 12, "bold"), bg="#4f46e5", fg="white", relief="flat", cursor="hand2").place(x=720, y=494, width=305, height=43)
        Button(self.register_frame, text="Back to login", command=lambda: self.show_frame(self.login_frame), font=("Segoe UI", 11), bg="white", fg="#334155", relief="flat", cursor="hand2").place(x=370, y=494, width=305, height=43)

    def create_dashboard(self):
        Label(self.dashboard_frame, text="LEARNSPACE", font=("Segoe UI", 13, "bold"), bg="#f4f7fc", fg="#4f46e5").place(x=70, y=46)
        Label(self.dashboard_frame, text="Your learning dashboard", font=("Segoe UI", 32, "bold"), bg="#f4f7fc", fg="#14213d").place(x=70, y=110)
        Label(self.dashboard_frame, text="Everything you need for your courses, all in one place.", font=("Segoe UI", 12), bg="#f4f7fc", fg="#64748b").place(x=70, y=167)
        sections = [
            ("01", "Browse courses", "Explore course materials", self.courses_frame),
            ("02", "Registration", "Enroll in a new course", self.registration_frame),
            ("03", "Assessments", "Check your results", self.assessment_frame),
            ("04", "Support tickets", "Get help with issues", self.supportTicket_frame),
        ]
        for i, (number, title, caption, target) in enumerate(sections):
            x = 70 + (i % 2) * 650
            y = 250 + (i // 2) * 144
            card = Frame(self.dashboard_frame, bg="white", highlightbackground="#dfe5ef", highlightthickness=1)
            card.place(x=x, y=y, width=605, height=122)
            Label(card, text=number, bg="white", fg="#4f46e5", font=("Segoe UI", 13, "bold")).place(x=24, y=18)
            Label(card, text=title, bg="white", fg="#14213d", font=("Segoe UI", 17, "bold")).place(x=70, y=18)
            Label(card, text=caption, bg="white", fg="#64748b", font=("Segoe UI", 11)).place(x=70, y=57)
            Button(card, text="Open  →", command=lambda f=target: self.show_frame(f), bg="#eef2ff", fg="#4338ca", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2").place(x=468, y=77, width=110, height=30)
        Button(self.dashboard_frame, text="Log out", command=lambda: self.show_frame(self.login_frame), bg="white", fg="#334155", font=("Segoe UI", 11), relief="flat", cursor="hand2").place(x=1220, y=43, width=110, height=36)
        Button(self.dashboard_frame,text="My Profile",command=lambda: (self.show_frame(self.profile_frame),self.display_profile()),bg="#4F46E5",fg="white",font=("Arial", 12, "bold"),padx=20,pady=12,relief="flat",cursor="hand2").pack(pady=15)

    def create_courses(self):
        Label(self.courses_frame, text="Course catalogue", font=("Segoe UI", 30, "bold"), bg="#f4f7fc", fg="#14213d").pack(anchor="w", padx=110, pady=(55, 6))
        Label(self.courses_frame, text="Choose a course to view its learning materials.", font=("Segoe UI", 12), bg="#f4f7fc", fg="#64748b").pack(anchor="w", padx=110, pady=(0, 18))
        courses = self.course.display_courses()
        for course in courses:
            course_card = Frame(self.courses_frame, bg="white", highlightbackground="#dfe5ef", highlightthickness=1, padx=20, pady=12)
            course_card.pack(padx=110, pady=7, fill="x")
            Label(course_card, text=course["course_name"], bg="white", fg="#14213d", font=("Segoe UI", 16, "bold")).pack(side="left", anchor="w", padx=8)
            Button(course_card, text="View course  →", command=lambda c=course: self.create_viewCourse(c), font=("Segoe UI", 11, "bold"), bg="#4f46e5", fg="white", relief="flat", cursor="hand2", padx=16, pady=7).pack(side="right")
        Button(self.courses_frame, text="← Back", command=lambda: self.show_frame(self.dashboard_frame), font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat").place(x=16, y=15, width=100, height=36)

    def create_viewCourse(self, course):
        course_name = course["course_name"]
        course_data = self.course.display_course_material(course_name)
        if course_data is None:
            return
        for widget in self.viewCourse_frame.winfo_children():
            widget.destroy()
        Label(self.viewCourse_frame, text=course_data["course_name"], font=("Segoe UI", 30, "bold"), bg="#f4f7fc", fg="#14213d").pack(pady=(60, 22))
        for heading, content in (("About this course", course_data["course_description"]), ("Duration", course_data["duration"]), ("Course material", course_data["course_material"])):
            card = Frame(self.viewCourse_frame, bg="white", padx=28, pady=16, highlightbackground="#dfe5ef", highlightthickness=1)
            card.pack(padx=150, pady=9, fill="x")
            Label(card, text=heading, font=("Segoe UI", 12, "bold"), bg="white", fg="#4f46e5").pack(anchor="w")
            Label(card, text=content, font=("Segoe UI", 12), bg="white", fg="#334155", wraplength=930, justify="left").pack(anchor="w", pady=(7, 0))
        Button(self.viewCourse_frame, text="Back to courses", command=lambda: self.show_frame(self.courses_frame), font=("Segoe UI", 11, "bold"), bg="#4f46e5", fg="white", relief="flat", padx=20, pady=10).pack(pady=20)
        Button(self.viewCourse_frame, text="← Back", command=lambda: self.show_frame(self.courses_frame), font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat").place(x=16, y=15, width=100, height=36)
        self.show_frame(self.viewCourse_frame)

    def create_registration(self):
        Label(self.registration_frame, text="Course registration", font=("Segoe UI", 30, "bold"), bg="#f4f7fc", fg="#14213d").place(x=345, y=62)
        Label(self.registration_frame, text="Select a course and enter your email to register.", font=("Segoe UI", 12), bg="#f4f7fc", fg="#64748b").place(x=347, y=122)
        Label(self.registration_frame, text="Available courses", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=347, y=177)
        self.registration_courses = self.course.display_courses()
        self.course_listbox = Listbox(self.registration_frame, width=50, height=9, font=("Segoe UI", 12), bg="white", fg="#14213d", selectbackground="#4f46e5", selectforeground="white", relief="solid", bd=1, activestyle="none")
        self.course_listbox.place(x=347, y=211, width=680, height=190)
        for course in self.registration_courses:
            self.course_listbox.insert(END, course["course_name"])
        Label(self.registration_frame, text="Email address", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=347, y=417)
        self.entryEmail = Entry(self.registration_frame, font=("Segoe UI", 12), bg="white", relief="solid", bd=1)
        self.entryEmail.place(x=347, y=446, width=680, height=40)
        Button(self.registration_frame, text="Register for course", command=self.register_selected_course, font=("Segoe UI", 12, "bold"), bg="#4f46e5", fg="white", relief="flat", cursor="hand2").place(x=347, y=506, width=680, height=43)
        Button(self.registration_frame, text="← Back", command=lambda: self.show_frame(self.dashboard_frame), font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat").place(x=16, y=15, width=100, height=36)

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
        Label(self.assessment_frame, text="My assessments", font=("Segoe UI", 30, "bold"), bg="#f4f7fc", fg="#14213d").place(x=355, y=57)
        Label(self.assessment_frame, text="Look up your marks and assessment results.", font=("Segoe UI", 12), bg="#f4f7fc", fg="#64748b").place(x=357, y=112)
        Label(self.assessment_frame, text="Learner ID", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=357, y=165)
        self.entryLearnerID = Entry(self.assessment_frame, width=30, font=("Segoe UI", 12), bg="white", relief="solid", bd=1)
        self.entryLearnerID.place(x=357, y=194, width=480, height=40)
        Button(self.assessment_frame, text="View my marks", command=self.display_marks, font=("Segoe UI", 11, "bold"), bg="#4f46e5", fg="white", relief="flat", cursor="hand2").place(x=853, y=194, width=175, height=40)
        Label(self.assessment_frame, text="Assessment results", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=357, y=263)
        self.marks_text = Text(self.assessment_frame, width=65, height=15, font=("Consolas", 11), bg="white", fg="#334155", padx=18, pady=16, relief="solid", bd=1)
        self.marks_text.place(x=357, y=296, width=671, height=250)
        Button(self.assessment_frame, text="← Back", command=lambda: self.show_frame(self.dashboard_frame), font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat").place(x=16, y=15, width=100, height=36)

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
        Label(self.supportTicket_frame, text="Contact support", font=("Segoe UI", 30, "bold"), bg="#f4f7fc", fg="#14213d").place(x=357, y=43)
        Label(self.supportTicket_frame, text="Describe your issue and we'll help you resolve it.", font=("Segoe UI", 12), bg="#f4f7fc", fg="#64748b").place(x=359, y=100)
        Label(self.supportTicket_frame, text="Learner email", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=359, y=152)
        self.entryTicketEmail = Entry(self.supportTicket_frame, width=30, font=("Segoe UI", 12), relief="solid", bd=1, bg="white")
        self.entryTicketEmail.place(x=359, y=179, width=670, height=40)
        Label(self.supportTicket_frame, text="Ticket category", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=359, y=236)
        self.ticket_type_list = Listbox(self.supportTicket_frame, width=30, height=3, font=("Segoe UI", 11), exportselection=False, bg="white", fg="#334155", selectbackground="#4f46e5", selectforeground="white", relief="solid", bd=1)
        self.ticket_type_list.insert(END, "Technical")
        self.ticket_type_list.insert(END, "Registration")
        self.ticket_type_list.insert(END, "Course")
        self.ticket_type_list.place(x=359, y=263, width=670, height=85)
        Label(self.supportTicket_frame, text="Description", font=("Segoe UI", 11, "bold"), bg="#f4f7fc", fg="#334155").place(x=359, y=363)
        self.ticket_description = Entry(self.supportTicket_frame, font=("Segoe UI", 11), relief="solid", bd=1, bg="white")
        self.ticket_description.place(x=359, y=391, width=670, height=43)
        Button(self.supportTicket_frame, text="Submit support ticket", command=self.submit_ticket, font=("Segoe UI", 12, "bold"), bg="#4f46e5", fg="white", relief="flat", cursor="hand2").place(x=359, y=461, width=670, height=46)
        Button(self.supportTicket_frame, text="← Back", command=lambda: self.show_frame(self.dashboard_frame), font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat").place(x=16, y=15, width=100, height=36)

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
    
    
    def create_profile(self):
        self.profile_frame.configure(bg="#F4F6FB")

        # Header
        header = Frame(self.profile_frame, bg="#18243D", height=100)
        header.pack(fill="x")
        header.pack_propagate(False)

        Label(
            header,
            text="My Learner Profile",
            font=("Arial", 25, "bold"),
            bg="#18243D",
            fg="white"
        ).pack(side="left", padx=40, pady=25)

        Button(
            header,
            text="Back to Dashboard",
            command=lambda: self.show_frame(self.dashboard_frame),
            bg="#334566",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            padx=15,
            pady=8
        ).pack(side="right", padx=40)

        # Main profile card
        card = Frame(
            self.profile_frame,
            bg="white",
            padx=40,
            pady=25,
            highlightbackground="#E0E5EF",
            highlightthickness=1
        )
        card.pack(pady=30, padx=50)

        Label(
            card,
            text="Personal Information",
            font=("Arial", 19, "bold"),
            bg="white",
            fg="#18243D"
        ).grid(row=0, column=0, columnspan=2,
            sticky="w", pady=(0, 15))

        Label(
            card,
            text="View and manage your account details",
            font=("Arial", 11),
            bg="white",
            fg="#68758B"
        ).grid(row=1, column=0, columnspan=2,
            sticky="w", pady=(0, 20))

        fields = [
            ("Email Address", "profile_email"),
            ("First Name", "profile_first_name"),
            ("Last Name", "profile_last_name"),
            ("Phone Number", "profile_phone"),
            ("New Password", "profile_password")
        ]

        for row_index, (label_text, attribute) in enumerate(
            fields, start=2
        ):
            Label(
                card,
                text=label_text,
                font=("Arial", 11, "bold"),
                bg="white",
                fg="#334155"
            ).grid(
                row=row_index,
                column=0,
                sticky="w",
                padx=(0, 25),
                pady=12
            )

            entry = Entry(
                card,
                font=("Arial", 12),
                width=37,
                relief="solid",
                bd=1,
                bg="#F8FAFC"
            )

            if attribute == "profile_password":
                entry.configure(show="*")

            entry.grid(
                row=row_index,
                column=1,
                padx=10,
                pady=12,
                ipady=7
            )

            setattr(self, attribute, entry)

        # Email is used to identify the learner
        self.profile_email.configure(state="readonly")

        Label(
            card,
            text="Leave the password blank to keep your current password.",
            bg="white",
            fg="#64748B",
            font=("Arial", 10)
        ).grid(
            row=7, column=0, columnspan=2,
            pady=(8, 18)
        )

        actions = Frame(card, bg="white")
        actions.grid(row=8, column=0, columnspan=2, pady=15)

        Button(
            actions,
            text="View My Details",
            command=self.display_profile,
            bg="#E4EAF5",
            fg="#18243D",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(side="left", padx=8)

        Button(
            actions,
            text="Save Changes",
            command=self.save_profile,
            bg="#4F46E5",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(side="left", padx=8)


    def display_profile(self):
        # Email was stored by Learner.login()
        learner_id = self.learner.learner_id

        if not learner_id:
            messagebox.showerror(
                "Profile",
                "Please log in first."
            )
            return

        result = self.learner.viewDetails(learner_id)

        if not isinstance(result, dict):
            messagebox.showerror(
                "Error",
                "Unable to retrieve learner details."
            )
            return

        # Supports a flat learner object or a nested learner key.
        learner = result.get("learner", result)

        if not isinstance(learner, dict):
            messagebox.showerror(
                "Error",
                "Unexpected learner response."
            )
            return

        self.profile_email.configure(state="normal")
        self.profile_email.delete(0, END)
        self.profile_email.insert(
            0, learner.get("email", learner_id)
        )
        self.profile_email.configure(state="readonly")

        self.profile_first_name.delete(0, END)
        self.profile_first_name.insert(
            0, learner.get("first_name") or ""
        )

        self.profile_last_name.delete(0, END)
        self.profile_last_name.insert(
            0, learner.get("last_name") or ""
        )

        self.profile_phone.delete(0, END)
        self.profile_phone.insert(
            0, learner.get("phone_no",
                        learner.get("phone_number", "")) or ""
        )

        self.profile_password.delete(0, END)


    def save_profile(self):
        email = self.learner.email
        first_name = self.profile_first_name.get().strip()
        last_name = self.profile_last_name.get().strip()
        phone_number = self.profile_phone.get().strip()
        password = self.profile_password.get()

        if not email:
            messagebox.showerror(
                "Error", "Please log in first."
            )
            return

        if not first_name or not last_name or not phone_number:
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all required fields."
            )
            return

        result = self.learner.updateDetails(
            email,
            first_name,
            last_name,
            password,
            phone_number
        )

        if isinstance(result, dict) and (
            result.get("status") not in
            ("Failed", "Unsuccessful", "Error")
        ):
            messagebox.showinfo(
                "Success",
                "Profile updated successfully!"
            )

            self.profile_password.delete(0, END)
            self.display_profile()

        else:
            messagebox.showerror(
                "Error",
                "Unable to update profile."
            )
       







       



        



       




if __name__ == '__main__':
    app = LMS()
    app.mainloop()
