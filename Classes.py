from LMS_Database import sessionLocal
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import bcrypt 
import time
from Singleton import AppConfig


config = AppConfig()






class Learner():
    def __init__(self,learner_id, first_name, last_name, email, phone_number, password, confPass):
        self.learner_id= learner_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confPass = confPass
        self.phone_number = phone_number

    def register(self,first_name,last_name,email,password,confPass,phone_num):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confPass = confPass
        self.phone_number= phone_num

        if not all([self.first_name,self.last_name,self.email,self.password,self.confPass,self.phone_number]):
            return {
            "status": "Unsuccessful",
            "message": "Fill in the form"}
        elif self.password != self.confPass:
             return {
            "status": "Unsuccessful",
            "message": "Passwords do not match"
        }  
    
        else:
            try:
                hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())        
                data = {
                        "first_name": self.first_name,
                        "last_name": self.last_name,
                        "email": self.email,
                        "password": hashed_password.decode("utf-8"),
                        "phone_no": self.phone_number}
                
                print("Sending data to FastAPI...")
                print(data)
       
                try:
                    response = requests.post(f"{config.api_url}/learners",json= data, timeout=10)
                    response.raise_for_status()
                    print("Response received!")
                    
                    print("Response:", response.text)
                                                
                    if response.status_code == 200:
                        print("success")
                        return response.json()
                                        
                    else:
                        print(response.text)
                        return None

                except requests.exceptions.Timeout:
                  print("ERROR: Request timed out")

                except requests.exceptions.ConnectionError:
                   print("ERROR: Could not connect to FastAPI")

                except requests.exceptions.RequestException as e:
                       print("REQUEST ERROR:", e)
                   
                except Exception as e:
                       print("UNEXPECTED ERROR:", e)    
            except:Exception 

        


    def updateDetails(self):
        self.email = input("Enter current email: ")
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.password = input("Enter password: ")
        self.phone_number= input("Enter phone number: ")
        try:
            hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())
            data = {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "password": hashed_password.decode("utf-8"),
                    "phone_no": self.phone_number}
            try:
                response = requests.put(f"{config.api_url}/learners/{self.email}",json= data, timeout=10)
                response.raise_for_status()
                print("Response received!")
                print("Status:", response.status_code)
                print("Response:", response.text)
                                                            
                if response.status_code == 200:
                    print("success")
                    return response.json()
                                                    
                else:
                    print(response.text)
                    return None
            
            except requests.exceptions.Timeout:
                              print("ERROR: Request timed out")
            
            except requests.exceptions.ConnectionError:
                               print("ERROR: Could not connect to FastAPI")
            
            except requests.exceptions.RequestException as e:
                                   print("REQUEST ERROR:", e)
                               
            except Exception as e:
                                   print("UNEXPECTED ERROR:", e)    
        except:Exception 
            
    def viewDetails(self):
           self.email = input("Enter current email: ")
           try:
                response = requests.get(f"{config.api_url}/learners/{self.email}", timeout=10)     
                print("Status:", response.status_code)
                print("Response:", response.text)

                if response.status_code == 200:
                         learner = response.json
                         print(learner)
                else:
                       print("Error could not find learner")

           except requests.exceptions.ConnectionError:
                        print("ERROR: Could not connect to FastAPI")
           except Exception as e:
                        print("UNEXPECTED ERROR:", e)

    def login(self, email, password):
        self.email = email
        self.password = password
        
        

        data = {"email": email,
                "password": password}

        try:
            response = requests.post(f"{config.api_url}/login",json=data,timeout=10)
            print("Status:", response.status_code)
            print("Response text:", response.text)
            result = response.json()
            if response.status_code == 200:
                if result ["status"] == "Successful":
                        learner = result["learner"]
                        self.learner_id = learner["learner_id"]

                        print("Learner ID:",self.learner_id)
                        print("Email",learner["email"]) 
                        result = { "status":"Success",
                                            "message":"Logged in successfully"}
                        
                        return result

                        
                        
                        
                else:
                     return{
                            "status":"Failed",
                            "message":"Unable to Login"},None
            else:
               return{
                "status":"Failed",
                "message":"Unable to Login"}, None
        except requests.exceptions.Timeout:
           print(
            "Error",
            "Request timed out"),None

        except requests.exceptions.ConnectionError:
           print(
            "Error",
            "Could not connect to FastAPI"), None

        except Exception as e:
            print("UNEXPECTED ERROR:", e), None

class Course():
    def __init__(self, course_id, course_name,course_description, duration, price, course_material ):
        self.course_id = course_id
        self.course_description= course_description
        self.course_name = course_name 
        self.duration = duration
        self.course_material = course_material
        self.price = price
    def add_course_material():
        pass

    def display_courses(self):
           try:
               response = requests.get("http://127.0.0.1:8000/courses")

               if response.status_code ==200:
                    courses = response.json()
                    return courses
               else:
                     print("No courses available")  
               
           except requests.exceptions.ConnectionError:
                                            print("ERROR: Could not connect to FastAPI")
           except Exception as e:
                                            print("UNEXPECTED ERROR:", e)


                  
    def display_course_material(self, course_name):
       
        
        try:
            response = requests.get(f"{config.api_url}/course/{course_name}", timeout=10)     
            print("Status:", response.status_code)
            print("Response:", response.text)
        
            if response.status_code == 200:
                 course1 = response.json()
                 return course1
            else:
                print("Error could not find course")
        
        except requests.exceptions.ConnectionError:
                                print("ERROR: Could not connect to FastAPI")
        except Exception as e:
                                print("UNEXPECTED ERROR:", e)

    def update_course_material():


        pass








class Registration():
    def __init__(self, registration_id, learner, course, registration_date, status):
        self.registration_id = registration_id
        self.learner = Learner
        self.course = course
        self.registration_date = registration_date
        self.status = status

    def get_learners(self):
        response = requests.get(f"{config.api_url}/Get_learners", timeout=10)
        response.raise_for_status()
        self.learners = response.json()
       
       

    def add_registration(self,learner_id , learner_email, course_id):
        self.learner_email = learner_email
        self.course_id = course_id
        self.learner_id = learner_id


        try:
            
            
            
            
            data = {
                    "learner_id": self.learner_id,
                    "learner_email": self.learner_email,
                    "course_id":self.course_id
            }
                        
            try:

                response = requests.post(f"{config.api_url}/registration",json= data, timeout=10)
               
                
                result =response.json()
                return  result
                
                        

                
                            
            except requests.exceptions.Timeout:
                print("ERROR: Request timed out")
                            
            except requests.exceptions.ConnectionError:
                print("ERROR: Could not connect to FastAPI")
                            
            except requests.exceptions.RequestException as e:
                print("REQUEST ERROR:", e)
                                                
            except Exception as e:
                print("UNEXPECTED ERROR:", e)    
        except:Exception 

              
        

    def handle_cocurrency(self):

            successful = 0
            unsuccessful = 0
            

            with ThreadPoolExecutor(max_workers=config.max_workers) as executor:
                   futures = [
                          executor.submit(self.add_registration, learner)
                          for learner in self.learners
                   ]

                   for future in as_completed(futures):
                        learner, result = future.result()
                        print("RESULT:", result)

                        if result.get("status") == "Pending":
                            print(f"[SUCCESS] {learner['first_name']} {learner['last_name']} registered")
                            successful += 1   
                        else: 
                            print(f"[UNSECCESSFUL] {learner['first_name']} {learner['last_name']}\n user exists")
                            unsuccessful += 1

            print()
            print("REGISTRATION SUMMARY")
            print("-" * 60)
    
            print(f"Total Registrations: {successful + unsuccessful}")
            print(f"Successful: {successful}")
            print(f"Unsuccessful: {unsuccessful}")



        
    def cancel_registration():
        pass

  



