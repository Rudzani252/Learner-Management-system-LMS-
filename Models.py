from sqlalchemy import Column, Integer,String, DECIMAL, TIMESTAMP, ForeignKey, Enum, Text, text, LargeBinary
from sqlalchemy.orm import relationship
from LMS_Database import base 

class Learner(base):
    __tablename__ = "learners"

    learner_id = Column(Integer, primary_key=True, autoincrement= True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
    phone_no = Column(String(20), nullable=False)
    role_id = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    registrations = relationship("Registration", back_populates="learners")
    assessments = relationship( "Assessment", back_populates="learners")
    support_tickets = relationship("SupportTicket", back_populates="learners")
   


class Lecturer(base):
        __tablename__ = "lecturers"

        lecturer_id = Column(Integer, primary_key=True, autoincrement= True)
        first_name = Column(String(50), nullable=False)
        last_name = Column(String(50), nullable=False)
        email = Column(String(100), nullable=False)
        


        phone_no = Column(String(20), nullable=False)
        role_id = Column(Integer, default=2)
        

        assessments = relationship("Assessment", back_populates="lecturers")
        courses = relationship("Course",back_populates="lecturers")

   
class Course(base):
      __tablename__ = "courses"

      course_id =  Column(Integer, primary_key=True, autoincrement= True)

      lecturer_id = Column(Integer, ForeignKey("lecturers.lecturer_id"), nullable=True)
      course_name = Column(String(100), nullable=False)
      course_description = Column(String(500), nullable=False)
      course_material = Column(Text, nullable=True)
      duration = Column(String(10), nullable=False)
      price= Column(DECIMAL, nullable=False)
      course_materialPDF = Column(LargeBinary, nullable=True)

      registrations = relationship("Registration", back_populates="courses")
      assessments = relationship("Assessment", back_populates="courses")
    
      lecturers = relationship("Lecturer",back_populates="courses")


class Registration(base):
      __tablename__ = "registrations"

      registration_id = Column(Integer, primary_key=True, autoincrement= True)
      learner_id= Column(Integer, ForeignKey("learners.learner_id"), nullable=True)
      learner_email  = Column(String(50), nullable=False)
      course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=True)
      registration_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
      status = Column(Enum("Pending", "Confrim", "Cancelled"), default="Pending")

      learners = relationship("Learner",back_populates="registrations")
      courses = relationship("Course",back_populates="registrations")
      

class Assessment(base):
      __tablename__ = "assessments"
      assessment_id =  Column(Integer, primary_key=True, autoincrement= True)
      learner_id = Column(Integer, ForeignKey("learners.learner_id"), nullable=True)
      lecturer_id = Column(Integer, ForeignKey("lecturers.lecturer_id"), nullable=True)
      course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=True)
      assessment_name = Column(String(100), nullable=False)
      assessment_score = Column(DECIMAL, nullable=False)
      assessment_result = Column(String(30), nullable=False)
      assessment_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

      lecturers = relationship("Lecturer",back_populates="assessments")
      courses = relationship("Course",back_populates="assessments")
      learners = relationship("Learner", back_populates="assessments")

class SupportTicket(base):
      __tablename__ ="support_tickets"
      ticket_id = Column(Integer, primary_key=True, autoincrement= True)
      learner_id = Column(Integer, ForeignKey("learners.learner_id"), nullable=True)
      description = Column(Text, nullable=False)
      ticket_type = Column(String(100), nullable=False)  
      status = Column(Enum("Open", "In Progress", "Resolved"), default="Open")
      learner_email = Column(String(255),nullable=False)
      created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
      updated_at = Column(TIMESTAMP,server_default=text("CURRENT_TIMESTAMP"),onupdate=text("CURRENT_TIMESTAMP"))
      learners = relationship("Learner",back_populates="support_tickets")



