from fastapi import FastAPI
import uvicorn

from Learner_Router import router as learner_router
from Course_Router import router as course_router
from Registration_Router import router as registration_router 
from SupportTicketRouter import router as ticket_router
from AssessmentRouter import router as assessment_router

app = FastAPI()

app.include_router(learner_router)
app.include_router(course_router)
app.include_router(registration_router)
app.include_router(ticket_router)
app.include_router(assessment_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )