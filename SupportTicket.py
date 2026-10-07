from LMS_Database import sessionLocal
import requests
from datetime import datetime
from Singleton import AppConfig


config = AppConfig()

class SupportTicket():
    def __init__(self, learner_id,learner_email,ticket_type,  description, status):
        
        self.learner_id = learner_id
        self.learner_email = learner_email
        self.ticket_type = ticket_type
        self.ticket_description = description
        self.status = status
        self.date_created = datetime.now()
    
    def create_ticket(self, learner_id, learner_email, ticket_type, description): 
        self.learner_id = learner_id
        self.email = learner_email
        self.ticket_type = ticket_type
        self.ticket_description = description
        status = "Open"
        try:
            data = {
                    "learner_id": self.learner_id,
                    "learner_email": self.email,
                    "ticket_type": self.ticket_type,
                    "description": self.ticket_description,
                    "status": status}
            
            try:
                response = requests.post(f"{config.api_url}/supportTickets",json=data, timeout=10)
                result = response.json()
                
                return result
            except requests.exceptions.Timeout:
                            print("ERROR: Request timed out")
            except requests.exceptions.ConnectionError:
                    print("Could not connect to FastAPI")
            
        except Exception as e:
                    print("Error:", e)
            
          


class TechnicalTickets(SupportTicket):
    def get_details(self):
        return {
            "ticket_type": "Technical",
            "ticket_description":self.ticket_description,
            "status":self.status
        }

class RegistrationTickets(SupportTicket):
    def get_details(self):
        return {
            "ticket_type": "Registration",
            "ticket_description":self.ticket_description,
            "status":self.status
        }

class CourseTickets(SupportTicket):
    def get_details(self):
        return {
            "ticket_type": "Course",
            "ticket_description":self.ticket_description,
            "status":self.status
        }

class SupportTicketFactory:
    @staticmethod


    def create_ticket(learner_id, ticket_type, description, status, learner_email):
        if ticket_type.lower() == "technical":
            return TechnicalTickets(learner_id= learner_id,learner_email= learner_email,ticket_type="Technical",description = description, status =status)

        elif ticket_type.lower() == "registration":
            return RegistrationTickets(learner_id= learner_id,learner_email= learner_email,ticket_type="Registration",description = description, status =status)

        elif ticket_type.lower() == "course":
            return CourseTickets(learner_id= learner_id,learner_email= learner_email,ticket_type="Course",description = description, status =status)

        else:
            raise ValueError("Invalid support ticket type")


  

