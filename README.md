#Learning Management System (LMS)

## Overview
A Python-based Learning Management System (LMS) designed to manage learners, courses, registrations, assessments, and support tickets.

The application uses FastAPI to provide REST API services, MySQL for persistent data storage, SQLAlchemy ORM for database operations, and Tkinter for the desktop user interface.

## Features 
# Learner Management
- Learner registration
- Secure login
- Password hashing using bcrypt
- View learner details
- Update learner information
- Retrieve registered learners

# Course Management
- Create courses
- View available courses
- View individual course information
- Update course details
- Upload course material

# Course Registration
- Register learners for courses
- Validate learners and courses before registration
- Prevent duplicate course registrations
- Course capacity validation
- Transaction monitoring and logging
  
# Assessment Management
- Create learner assessments
- Calculate assessment percentages
- Determine Pass/Fail results
- Retrieve learner marks
- Associate assessments with learners, lecturers, and courses

# Support Ticket System
- Retrieve learner support tickets
- Support multiple ticket categories
- Track ticket status
- Supported ticket statuses include:

Open,
In Progress,
Resolved

# Technologies
- Python 3.11+
- FastAPI
- MySQL
- SQLAlchemy
- PyMySQL
- Tkinter
- Pydantic
- bcrypt
- Uvicorn
- Requests
- Pytest
- cProfile
- uv

# Architecture
Tkinter Desktop Application
          │
          │ HTTP Requests
          ▼
      FastAPI API
          │
          ▼
     SQLAlchemy ORM
          │
          ▼
       MySQL

FastAPI routers separate the major application features:
- Learner Router
- Course Router
- Registration Router
- Assessment Router
- Support Ticket Router

# Database Design
The LMS contains relational models for:
- Learners
- Lecturers
- Courses
- Registrations
- Assessments
- Support Tickets
- Foreign-key relationships connect learners, lecturers, courses, registrations, assessments, and support tickets.

# API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/learners` | Register a learner |
| POST | `/login` | Authenticate a learner |
| GET | `/learners/{learner_email}` | View learner details |
| PUT | `/learners/{learner_email}` | Update learner details |
| GET | `/Get_learners` | Retrieve learners |
| GET | `/courses` | Retrieve courses |
| GET | `/course/{course_name}` | View course information |
| PUT | `/course/{course_name}` | Update a course |
| POST | `/registration` | Register for a course |
| POST | `/assessment` | Create an assessment |
| GET | `/marks/{learner_id}` | Retrieve learner marks |
| POST | `/supportTickets` | Create a support ticket |
| GET | `/supportTickets/{learner_id}` | Retrieve learner tickets |

# Security 
- Learner passwords are hashed using bcrypt before being stored.

- During authentication, the supplied password is verified against the stored bcrypt hash.

The application also performs validation for scenarios such as:
- Duplicate email addresses
- Invalid login credentials
- Duplicate course registrations
- Missing learners
- Missing courses
- Invalid assessments
- Course capacity limits

#  Monitoring & Performance
The registration workflow includes application monitoring for:
- Successful and failed transactions
- Validation failures
- Duplicate registrations
- Course capacity violations
- Application errors
- Request processing time

  Python's cProfile is also used to profile registration requests and identify performance bottlenecks.

# Installation
1. Clone the repository:
   
git clone <your-repository-url>
cd <repository-name>
2. Install uv

If uv is not already installed:
pip install uv
3. Install dependencies

uv sync

4. Database Configuration
   
  Create a MySQL database for the LMS.

  Configure the following database values in the "database_config.py" file:

DATABASE,
USER,
PASSWORD,
HOST,
PORT

# Running the Application

1. Start the FastAPI backend:
   uv run uvicorn main:app --reload

   OR run the "main.py" file
2.  Run the Tkinter desktop application in a separate terminal:
   uv run python Tkinter.py

    OR run the "Tkinter.py" file
    
# Testing
The project includes testing and profiling utilities for application functionality such as registration, assessments, and support tickets.

Tests can be executed using:

uv run pytest

# Project Purpose 
This project was developed to demonstrate the implementation of an enterprise-style Learning Management System using Python.
The project focuses on:
- REST API development
- Relational database design
- Object-Oriented Programming
- Authentication and password security
- API-to-client communication
- Business-rule validation
- Error handling
- Application monitoring
- Performance profiling
- Software design patterns

# Future Improvements
- JWT-based authentication and authorization
- Role-based access control for learners, lecturers, and administrators
- Improved Tkinter user interface
- Database migrations using Alembic
- Expanded automated test coverage
- Docker containerization
- API pagination
- Deployment to a cloud platform
- CI/CD pipeline using GitHub Actions
