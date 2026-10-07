from fastapi import HTTPException, Depends, APIRouter, UploadFile,File,Form
from LMS_Database import get_db, engine
from sqlalchemy.orm import Session
from Models import Course
from pydantic import BaseModel
import python_multipart

router = APIRouter()



@router.post("/Add Course")
def add_coursePDF(
    course_name : str= Form(),
    course_description:str= Form(),
    duration: str= Form(),
    price: float = Form(),
    course_material: UploadFile = File(...),
    db:Session= Depends(get_db)):

    file_data = course_material.file.read()
    new_course = Course(
    course_name=course_name,
    course_description=course_description,
    duration=duration,
    price=price,
    course_material=file_data)

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return 



class ViewCourse(BaseModel):
   
    course_name : str 
    course_description: str
    duration :str 
    course_material: str

    class Config:
        from_attribute = True


@router.get("/course/{course_name}", response_model= ViewCourse)
def get_course(course_name: str, db:Session= Depends(get_db)):
    existing_course = db.query(Course).filter(Course.course_name == course_name).first()
    if not existing_course:
        raise HTTPException(
        status_code = 400,
        detail= "Course not found")

    return existing_course

@router.get("/courses")
def get_courses(db:Session =Depends(get_db)):
    courses = db.query(Course).all()
    return courses

@router.put("/update PDF/{course_name}")
def update_coursePDF(
    course_name : str, 
    course_description: str |None=  Form(None),
    duration: str |None=  Form(None),
    price: float |None=  Form(None),
    course_material: UploadFile = File(...),
    db:Session= Depends(get_db)):

    course = db.query(Course).filter(Course.course_name == course_name).first()
      
    
    if course_description is not None:
        course.course_description = course_description
    
    
    if duration is not None:
        course.duration = duration
    
    if price is not None:
        course.price = price

    if course_material is not None:
        file_data = course_material.file.read()
        course.course_material = file_data
    
    db.commit()
    db.refresh(course)

    file_data = course_material.file.read()
    new_course = Course(
        course_name=course_name,
        course_description=course_description,
        duration=duration,
        price=price,
        course_material=file_data)
    

    return course


class UpdateCourse(BaseModel):
    course_name : str|None =None
    course_description :str |None =None
    duration :str |None =None
    price: str |None=None

@router.put("/course/{course_name}")
def update_learner(course_name: str, course: UpdateCourse, db:Session = Depends(get_db)):
    existing_course1 = db.query(Course).filter(Course.course_name== course_name).first()
    if not existing_course1:
        raise HTTPException(
        status_code = 400,
        detail= "Course not found")

    if course.course_name is not None:
        existing_course1.course_name = course.course_name  

    if course.course_description is not None:
        existing_course1.course_description = course.course_description


    if course.duration is not None:
        existing_course1.duration = course.duration

    if course.price is not None:
        existing_course1.price = course.price

    db.commit()
    db.refresh(existing_course1)
    return existing_course1


