from fastapi import FastAPI, Depends,  APIRouter
from LMS_Database import get_db, engine
from sqlalchemy.orm import Session
from model import SupportTicket as SupportTicketModel
from pydantic import BaseModel
from enum import Enum
from SupportTicket import SupportTicketFactory



router = APIRouter()




class RegistrationStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"


class AddSupportTicket(BaseModel):
    learner_id : int
    description: str 
    ticket_type :str 
    status: RegistrationStatus
    learner_email: str
    

@router.post("/supportTickets")
def add_support_ticket(supportTicket: AddSupportTicket, db:Session= Depends(get_db)):
    try:
        created_ticket = SupportTicketFactory.create_ticket(learner_id=supportTicket.learner_id,
            description=supportTicket.description,                                              
            ticket_type=supportTicket.ticket_type,
            status=supportTicket.status.value,
            learner_email=supportTicket.learner_email)
        
        new_support_ticket = SupportTicketModel(
            learner_id=created_ticket.learner_id,
            description=created_ticket.ticket_description,
            ticket_type=created_ticket.ticket_type,
            status=created_ticket.status,
            learner_email=created_ticket.learner_email)
        
        db.add(new_support_ticket)
        db.commit()
        db.refresh(new_support_ticket)
        return new_support_ticket
    except ValueError as e:
        return {
            "status": "Failed",
            "message": str(e) }

    except Exception as e:
        db.rollback()

        return {
            "status": "Failed",
            "message": str(e)}

@router.get("/supportTickets/{learner_id}")
def view_tickets(
    learner_id: int,
    db: Session = Depends(get_db)
):

    tickets = db.query(SupportTicketModel).filter(
        SupportTicketModel.learner_id == learner_id
    ).all()

    if not tickets:
        return {
            "status": "Not Found",
            "message": "No support tickets found"
        }

    return tickets

      