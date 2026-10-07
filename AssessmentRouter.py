from fastapi import FastAPI, Depends, APIRouter
from LMS_Database import get_db, engine
from sqlalchemy.orm import Session
from model import Assessment, Learner, Course, Lecturer
from pydantic import BaseModel
import datetime



router= APIRouter()



class addAssessment(BaseModel):

        learner_id: int
        lecturer_id: int
        course_id: int
        assessment_name: str
        assessment_score: float
        maximum_mark: float

@router.post("/assessment")
def add_assessment(assessment:addAssessment, db:Session= Depends(get_db)):
    learner = db.query(Learner).filter(
        Learner.learner_id == assessment.learner_id).first()
    

    if not learner:
        return {
            "status": "Failed",
            "message": "Learner does not exist"
        }
    lecturer = db.query(Lecturer).filter(
        Lecturer.lecturer_id == assessment.lecturer_id).first()
    
    if not lecturer:
           return {
            "status": "Failed",
            "message": "Lecturer does not exist"
        }
    course = db.query(Course).filter(
        Course.course_id == assessment.course_id).first()
    if not course:
        return {
            "status": "Failed",
            "message": "Course does not exist"
        }
    if assessment.maximum_mark <= 0:
        return {
            "status": "Failed",
            "message": "Maximum mark must be greater than zero"
        }
    
    percentage = (
        assessment.assessment_score /assessment.maximum_mark) * 100

    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"
    new_assessment = Assessment(
        learner_id=learner.learner_id,
        lecturer_id = assessment.lecturer_id,
        course_id=assessment.course_id,
        assessment_name=assessment.assessment_name,
        assessment_score=assessment.assessment_score,
        assessment_result=result,
        assessment_date=datetime.datetime.now()
    )
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)
    return new_assessment 

@router.get("/marks/{learner_id}")
def get_marks(learner_id: int,db: Session = Depends(get_db)):

    assessments = db.query(Assessment).filter(
        Assessment.learner_id == learner_id).all()

    if not assessments:
        return {
            "status": "Not Found",
            "message": "No marks found for this learner"
        }

    return assessments
