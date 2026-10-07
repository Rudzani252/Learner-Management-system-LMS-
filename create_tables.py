from LMS_Database import engine, base 
import Models

base.metadata.create_all(bind=engine)