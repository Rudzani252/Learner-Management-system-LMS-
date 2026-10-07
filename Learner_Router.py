from fastapi import Depends, HTTPException, APIRouter
from LMS_Database import get_db, engine
from sqlalchemy.orm import Session
from model import Learner
from pydantic import BaseModel, ConfigDict
import bcrypt



router = APIRouter()



class addLearners(BaseModel):
    first_name : str
    last_name :str
    email :str
    password: str
    phone_no :str


@router.post("/learners")
def add_learner(learner:addLearners, db:Session= Depends(get_db)):

    existing_email = db.query(Learner).filter(Learner.email== learner.email).first()
    if existing_email:
        raise HTTPException(
            status_code = 400,
            detail= "Email already exists"
        )

    existing_name = db.query(Learner).filter(Learner.first_name == learner.first_name,
                                             Learner.last_name == learner.last_name).first()

    if existing_name:
        raise HTTPException(status_code = 400,detail= "Learner with this name already exists")
    
        

    
     
    new_learner = Learner(first_name= learner.first_name, last_name= learner.last_name, email= learner.email,password = learner.password, phone_no = learner.phone_no)



    db.add(new_learner)
    db.commit()
    db.refresh(new_learner)
    return new_learner 


class UpdateLearner(BaseModel):
    first_name : str|None =None
    last_name :str |None =None
    email: str | None = None
    password: str |None =None
    phone_no :str |None =None

@router.put("/learners/{learner_email}")
def update_learner(learner_email: str, learner: UpdateLearner, db:Session = Depends(get_db)):
    existing_learner = db.query(Learner).filter(Learner.email== learner_email).first()
    if not existing_learner:
        raise HTTPException(
        status_code = 400,
        detail= "Email not found")

    if learner.first_name is not None:
        existing_learner.first_name = learner.first_name

    if learner.last_name is not None:
        existing_learner.last_name = learner.last_name


    if learner.phone_no is not None:
        existing_learner.phone_no = learner.phone_no

    if learner.password is not None:
        existing_learner.password = learner.password

    db.commit()
    db.refresh(existing_learner)
    return existing_learner


class ViewDetails(BaseModel):
    first_name : str
    last_name :str
    email :str
    phone_no :str

    class Config:
        from_attribute = True

@router.get("/learners/{learner_email}", response_model=ViewDetails)
def get_learner_details(learner_email:str, db:Session = Depends(get_db)):
    existing_learner = db.query(Learner).filter(Learner.email== learner_email).first()
    if not existing_learner:
            raise HTTPException(
            status_code = 400,
            detail= "Email not found")

    return existing_learner




class ViewLearners(BaseModel):
    learner_id :int
    first_name : str
    last_name :str
    email :str
    phone_no :str

    model_config = ConfigDict(from_attributes=True)


@router.get("/Get_learners", response_model=list[ViewLearners])
def get_learners(db:Session = Depends(get_db)):
    learners = db.query(Learner).all()
    return learners


class LoginRequest(BaseModel):
    email :str 
    password :str 

@router.post("/login")
def login_user(login:LoginRequest, db:Session= Depends(get_db)):
    learner = db.query(Learner).filter(
        Learner.email == login.email).first()
    if not learner:
        return {"status": "Unsuccessful",
                "message":"Invalid email or password"}
    stored_password = learner.password

    if isinstance(stored_password, str):
        stored_password = stored_password.encode("utf-8")

    password_correct = bcrypt.checkpw(
        login.password.encode("utf-8"),
        stored_password
    )

    if not password_correct:
        return {"status": "Unsuccessful",
                "message":"Invalid email or password"}

    return {
        "status": "Successful",
        "message": "Logged in successfully",

        "learner": {
            "learner_id": learner.learner_id,
            "email": learner.email,
            "first_name": learner.first_name,
            "last_name": learner.last_name
        }
    }
