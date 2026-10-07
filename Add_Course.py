import requests
from LMS_Database import sessionLocal

class Course():
    def __init__(self,  course_name,course_description, duration, price, course_material ):
        self.course_description= course_description
        self.course_name = course_name 
        self.duration = duration
        self.course_material = course_material
        self.price = price
    def add_course_material():
        pass
    def display_course_material(self):
       
        self.course_name = input("Enter course name: ")
        try:
            response = requests.get(f"http://127.0.0.1:8000/course/{self.course_name}", timeout=10)     
            print("Status:", response.status_code)
            print("Response:", response.text)
        
            if response.status_code == 200:
                 course1 = response.json
                 print(course1)
            else:
                print("Error could not find learner")
        
        except requests.exceptions.ConnectionError:
                                print("ERROR: Could not connect to FastAPI")
        except Exception as e:
                                print("UNEXPECTED ERROR:", e)

    def update_course_material():


        pass

course2 = Course(course_name="",course_description="",
        duration ="",
        price="",
        course_material="")

course2.display_course_material()
