from abc import ABC, abstractmethod
import requests
from Singleton import AppConfig
from LMS_Database import sessionLocal

config = AppConfig()

class Assessment():
    def __init__(self,learner_id, course_id, assessment_name,score, result):
        self.learner = learner_id 
        self.assessment_name = assessment_name
        self.course = course_id
        self.score = score 
        self.result = result 

    
    class AssessmentStrategy(ABC):
        @abstractmethod
        def get_marks(self, marks, maximum_mark):
            return marks, maximum_mark
        def get_marks(self, marks, maximum_mark):
            marks = int(input("Enter learner's mark: "))
            maximum_mark = int(input('enter assignment totol marks'))
            return marks, maximum_mark

    class PercentageStrategy(AssessmentStrategy):
        def get_marks(self, marks, maximum_mark):
            return marks, maximum_mark
        def calculate_percentage(self, marks, maximum_mark):
            
            maximum_mark = maximum_mark
            learner_percentage = (marks / maximum_mark)*100
            return learner_percentage

    class PassFailStrategy(AssessmentStrategy):
        def check_pass_or_fail(self, marks, maximum_mark):
            avarage = (marks/maximum_mark)*100

            if avarage >=50:
                return "Pass"

            else: 
                return "Fail"

    class weightedStrategy(AssessmentStrategy):
        def get_marks(self, marks, maximum_mark):
            return marks, maximum_mark
        def calculate_weight(self, marks):
            assignment = marks["assignment"] * 0.40
            test = marks["test"] * 0.10
            exam = marks["exam"] * 0.50
            return assignment + test + exam

            
    def get_marks(self, learner_id):
        self.learner_id = learner_id
        data = {"learner_id":self.learner_id}
        try:
            response = requests.get(f"{config.api_url}/marks/{learner_id}",timeout=10)
            if response.status_code == 200:
                marks = response.json()
                return marks
            else:
                print("Error could not find learner")

            return response.json()

        except requests.exceptions.ConnectionError:
            print("Could not connect to FastAPI")
        

        except requests.exceptions.Timeout:
                print("Request timed out")
            

        except Exception as e:
            print("Error:", e)
            


        

   

def create_assessment_from_input():

    print("\nCREATE ASSESSMENT")
    print("-" * 50)
    learner_id = int(input("Enter learner ID: "))
    learner_email = input("Enter learner email: ")
    lecturer_id = int(input("Enter lecturer ID: "))
    course_id = int(input("Enter course ID: "))
    assessment_name = input("Enter assessment name: ")

    assessment_score = float(
        input("Enter learner's mark: ")
    )

    maximum_mark = float(
        input("Enter maximum mark: ")
    )

    data = {
        "learner_id": learner_id,
        "learner_email": learner_email,
        "lecturer_id": lecturer_id,
        "course_id": course_id,
        "assessment_name": assessment_name,
        "assessment_score": assessment_score,
        "maximum_mark": maximum_mark
    }

    try:
        print("\nSending assessment to FastAPI...")

        response = requests.post(f"{config.api_url}/assessment",json=data, timeout=10)

        result = response.json()

        print("\nASSESSMENT RESULT")
        print("-" * 50)
        print("Status Code:", response.status_code)
        print("Learner Email:", learner_email)
        print("Lecturer ID:", lecturer_id)
        print("Course ID:", course_id)
        print("Assessment:", assessment_name)
        print("Score:", assessment_score)
        print("Maximum Mark:", maximum_mark)
        print("-" * 50)

        print("FastAPI Response:")
        print(result)

        return result

    except requests.exceptions.Timeout:
        print("ERROR: Request timed out")

    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to FastAPI")

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    create_assessment_from_input()