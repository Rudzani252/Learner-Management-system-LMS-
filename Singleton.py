from database_config import DATABASE, USER, PASSWORD, HOST, PORT
user = USER
password = PASSWORD
database = DATABASE
port = PORT
host = HOST


class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__()


        return cls._instance[cls]

class AppConfig(metaclass=SingletonMeta):
    
    def __init__(self):
        
        self.api_url = "http://127.0.0.1:8000"
        self.course_capacity = 500
        self.max_workers = 10 
        self.request_time = 10 
        self.database_url = (f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

