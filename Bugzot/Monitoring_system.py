import logging
import time
from datetime import datetime

 


bugzot = logging.getLogger("Bugzot")
bugzot.setLevel(logging.INFO)
handler = logging.FileHandler("bugzot.log")
formatter = logging.Formatter(" %(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
bugzot.addHandler(handler)

total_transactions = 0
successful_transactions = 0
failed_transactions = 0

total_processing_time = 0
fastest_transaction = None
slowest_transaction = 0

def log_validation_failure(field, reason, learner_id):
    bugzot.warning(f"VALIDATION FAILURE| Field:{field}|Student ID: {learner_id}| Reason: {reason}")

def log_dup_registration(learner_id, course_name):
    bugzot.warning(f"DUPLICATE REGISTRATION| Course:{course_name}|Student ID: {learner_id}|Registration rejected")

def log_course_capacity_violation(learner_id, course_name, course_capacity):
    bugzot.warning(f"COURSE CAPACITY VIOLATION| Course:{course_name}|Student ID: {learner_id}|Maximum capacity: {course_capacity}| Full")

def log_application_error(error_type, message):
    bugzot.error(
        f"APPLICATION ERROR | "
        f"Type: {error_type} | "
        f"Message: {message}"
    )

def record_transaction(processing_time, successful=True):

    global total_transactions
    global successful_transactions
    global failed_transactions
    global total_processing_time
    global fastest_transaction
    global slowest_transaction

    total_transactions += 1

    total_processing_time += processing_time

    if successful:
        successful_transactions += 1
    else:
        failed_transactions += 1

    if fastest_transaction is None:
        fastest_transaction = processing_time

    elif processing_time < fastest_transaction:
        fastest_transaction = processing_time

    if processing_time > slowest_transaction:
        slowest_transaction = processing_time

    bugzot.info(
        f"TRANSACTION | "
        f"Successful: {successful} | "
        f"Processing Time: {processing_time:.4f} seconds"
    )

    def generate_performance_report():

        if total_transactions > 0:
            average_processing_time = (
                total_processing_time /
                total_transactions
            )
        else:
            average_processing_time = 0

        fastest = fastest_transaction or 0
        report = f"""
                    BUGZOT PERFORMANCE REPORT\n
                    Generated: {datetime.now()}\n
                    TRANSACTION ACTIVITY
                    ----------------------------------------
                    Total Transactions: {total_transactions}

                    Successful Transactions:
                    {successful_transactions}

                    Failed Transactions:
                    {failed_transactions}


                    PROCESSING PERFORMANCE
                    ----------------------------------------
                    Average Processing Time:
                    {average_processing_time:.4f} seconds

                    Fastest Transaction:
                    {fastest:.4f} seconds

                    Slowest Transaction:
                    {slowest_transaction:.4f} seconds


                    """
        with open(
            "bugzot_performance_report.txt",
            "w"
        ) as file:
            file.write(report)

            return report


def log_success(event, details):
    bugzot.info(
        f"SUCCESS | "
        f"Event: {event} | "
        f"Details: {details}"
    )

    
