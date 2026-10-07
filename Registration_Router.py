from fastapi import  Depends, HTTPException, APIRouter
from LMS_Database import get_db, engine
from sqlalchemy.orm import Session
from model import Learner, Course, Registration
from pydantic import BaseModel
from Singleton import AppConfig
from Bugzot.models import (
    log_validation_failure,
    log_dup_registration,
    log_course_capacity_violation,
    log_application_error,
    log_success,
    record_transaction
)
import time 

config = AppConfig()

router = APIRouter()

class addRegistration(BaseModel):
    learner_id :int
    learner_email: str
    course_id: int


@router.post("/registration")
def register_leaner(registration: addRegistration, db:Session = Depends(get_db)):
    start_time = time.perf_counter()
    try:
        learner = db.query(Learner).filter(
                Learner.email == registration.learner_email).first()
        
        if not learner:
            processing_time = (time.perf_counter() -start_time)
            record_transaction(processing_time,successful=False)
            
            log_validation_failure(
            field="learner_email",
            reason="Learner email does not exist",
            learner_id="Unknown")

            return {"status":"Unable to Register",
                    "message": "Email does not exist"}

        course = db.query(Course).filter(
            Course.course_id == registration.course_id).first()
        if not course:
                return {"status":"Unable to Register",
                            "message": "Course does not exist"}

        existiing_registration = db.query(Registration).filter(
                Registration.learner_id == registration.learner_id,
                Registration.course_id == registration.course_id).first()


        if existiing_registration:
                
            log_dup_registration(
            learner_id=learner.learner_id,
            course_name=course.course_name)
            processing_time = (time.perf_counter() -start_time)
            record_transaction(processing_time,successful=False)
                
            return{
                    "status": "Unseccessful",
                    "message": "Learner is already registered for this course"
                }

        register_count = db.query(Registration).filter(
                Registration.course_id == registration.course_id,
                Registration.status == "Successful").count()

        if register_count >= config.course_capacity:
            processing_time = (time.perf_counter() -start_time)
            record_transaction(processing_time,successful=False)

            log_course_capacity_violation(
            learner_id=learner.learner_id,
            course_name=course.course_name,
            course_capacity=500)

            return {
            "status": "Unsuccessful",
            "message": "Course is full. Maximum capacity is 500 learners."}
        else:
                new_registeration = Registration(learner_id = registration.learner_id,learner_email= registration.learner_email, course_id = registration.course_id)
                db.add(new_registeration)
                db.commit()
                db.refresh(new_registeration)
                processing_time = (time.perf_counter() -start_time)
                record_transaction(processing_time,successful=False)
                log_success(event="Registration",details=(f"Learner ID: {learner.learner_id}, "f"Course: {course.course_name}"))
                return new_registeration
                
    except Exception as e:

        db.rollback()

        log_application_error(
            error_type=type(e).__name__,
            message=str(e)
        )

        return {
            "status": "Failed",
            "message": "An application error occurred"
        }
    